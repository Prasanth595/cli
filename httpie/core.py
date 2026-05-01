import argparse
import base64
import io
import json
import os
import platform
import sys
import socket
import tempfile
from datetime import datetime, timezone
from time import monotonic
from typing import Any, Dict, List, Optional, Union, Callable

import requests
from pygments import __version__ as pygments_version
from requests import __version__ as requests_version

from . import __version__ as httpie_version
from .cli.constants import OUT_REQ_BODY
from .cli.nested_json import NestedJSONSyntaxError
from .client import collect_messages
from .context import Environment, LogLevel
from .downloads import Downloader
from .models import (
    RequestsMessageKind,
    OutputOptions
)
from .output.models import ProcessingOptions
from .output.writer import write_message, write_stream, write_raw_data, MESSAGE_SEPARATOR_BYTES
from .plugins.registry import plugin_manager
from .status import ExitStatus, http_status_to_exit_status
from .utils import unwrap_context
from .internal.update_warnings import check_updates
from .internal.daemon_runner import is_daemon_mode, run_daemon_task


# noinspection PyDefaultArgument
def raw_main(
    parser: argparse.ArgumentParser,
    main_program: Callable[[argparse.Namespace, Environment], ExitStatus],
    args: List[Union[str, bytes]] = sys.argv,
    env: Environment = Environment(),
    use_default_options: bool = True,
) -> ExitStatus:
    program_name, *args = args
    env.program_name = os.path.basename(program_name)
    args = decode_raw_args(args, env.stdin_encoding)

    if is_daemon_mode(args):
        return run_daemon_task(env, args)

    plugin_manager.load_installed_plugins(env.config.plugins_dir)

    if use_default_options and env.config.default_options:
        args = env.config.default_options + args

    include_debug_info = '--debug' in args
    include_traceback = include_debug_info or '--traceback' in args

    def handle_generic_error(e, annotation=None):
        msg = str(e)
        if hasattr(e, 'request'):
            request = e.request
            if hasattr(request, 'url'):
                msg = (
                    f'{msg} while doing a {request.method}'
                    f' request to URL: {request.url}'
                )
        if annotation:
            msg += annotation
        env.log_error(f'{type(e).__name__}: {msg}')
        if include_traceback:
            raise

    if include_debug_info:
        print_debug_info(env)
        if args == ['--debug']:
            return ExitStatus.SUCCESS

    exit_status = ExitStatus.SUCCESS

    try:
        parsed_args = parser.parse_args(
            args=args,
            env=env,
        )
    except NestedJSONSyntaxError as exc:
        env.stderr.write(str(exc) + "\n")
        if include_traceback:
            raise
        exit_status = ExitStatus.ERROR
    except KeyboardInterrupt:
        env.stderr.write('\n')
        if include_traceback:
            raise
        exit_status = ExitStatus.ERROR_CTRL_C
    except SystemExit as e:
        if e.code != ExitStatus.SUCCESS:
            env.stderr.write('\n')
            if include_traceback:
                raise
            exit_status = ExitStatus.ERROR
    else:
        check_updates(env)
        try:
            exit_status = main_program(
                args=parsed_args,
                env=env,
            )
        except KeyboardInterrupt:
            env.stderr.write('\n')
            if include_traceback:
                raise
            exit_status = ExitStatus.ERROR_CTRL_C
        except SystemExit as e:
            if e.code != ExitStatus.SUCCESS:
                env.stderr.write('\n')
                if include_traceback:
                    raise
                exit_status = ExitStatus.ERROR
        except requests.Timeout:
            exit_status = ExitStatus.ERROR_TIMEOUT
            env.log_error(f'Request timed out ({parsed_args.timeout}s).')
        except requests.TooManyRedirects:
            exit_status = ExitStatus.ERROR_TOO_MANY_REDIRECTS
            env.log_error(
                f'Too many redirects'
                f' (--max-redirects={parsed_args.max_redirects}).'
            )
        except requests.exceptions.ConnectionError as exc:
            annotation = None
            original_exc = unwrap_context(exc)
            if isinstance(original_exc, socket.gaierror):
                if original_exc.errno == socket.EAI_AGAIN:
                    annotation = '\nCouldn’t connect to a DNS server. Please check your connection and try again.'
                elif original_exc.errno == socket.EAI_NONAME:
                    annotation = '\nCouldn’t resolve the given hostname. Please check the URL and try again.'
                propagated_exc = original_exc
            else:
                propagated_exc = exc

            handle_generic_error(propagated_exc, annotation=annotation)
            exit_status = ExitStatus.ERROR
        except Exception as e:
            # TODO: Further distinction between expected and unexpected errors.
            handle_generic_error(e)
            exit_status = ExitStatus.ERROR

    return exit_status


def main(
    args: List[Union[str, bytes]] = sys.argv,
    env: Environment = Environment()
) -> ExitStatus:
    """
    The main function.

    Pre-process args, handle some special types of invocations,
    and run the main program with error handling.

    Return exit status code.

    """

    from .cli.definition import parser

    return raw_main(
        parser=parser,
        main_program=program,
        args=args,
        env=env
    )





def _normalize_headers(headers: Dict[str, Any]) -> Dict[str, str]:
    normalized = {}
    for key, value in headers.items():
        key_str = str(key)
        if isinstance(value, bytes):
            normalized[key_str] = value.decode('utf-8', errors='replace')
        elif isinstance(value, str):
            normalized[key_str] = value
        else:
            normalized[key_str] = str(value)
    return normalized


def _serialize_request_body(body: Any) -> Dict[str, str]:
    result = {}
    if body is None:
        return result
    
    if isinstance(body, bytes):
        try:
            result['body'] = body.decode('utf-8', errors='replace')
        except Exception:
            result['body_base64'] = base64.b64encode(body).decode('ascii')
    elif isinstance(body, str):
        result['body'] = body
    elif isinstance(body, dict):
        try:
            result['body'] = json.dumps(body, ensure_ascii=False, default=str)
        except Exception:
            result['body'] = str(body)
    else:
        try:
            result['body'] = str(body)
        except Exception:
            pass
    
    return result


def _collect_metadata(
    initial_request: Optional[requests.PreparedRequest],
    final_response: Optional[requests.Response],
    response_body_preview: Optional[bytes],
    args: Optional[argparse.Namespace] = None,
) -> dict:
    metadata = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
    }

    if initial_request:
        request_data = {
            'method': initial_request.method,
            'url': initial_request.url,
            'headers': _normalize_headers(dict(initial_request.headers)),
        }
        
        if hasattr(args, 'data') and args.data is not None:
            request_data.update(_serialize_request_body(args.data))
        elif initial_request.body is not None:
            request_data.update(_serialize_request_body(initial_request.body))
        
        metadata['request'] = request_data

    if final_response:
        metadata['response'] = {
            'status_code': final_response.status_code,
            'headers': _normalize_headers(dict(final_response.headers)),
        }

        if response_body_preview:
            preview_bytes = response_body_preview[:1024]
            try:
                metadata['response']['body_preview'] = preview_bytes.decode('utf-8', errors='replace')
            except Exception:
                metadata['response']['body_preview_base64'] = base64.b64encode(preview_bytes).decode('ascii')

        try:
            time_to_parse_headers = final_response.elapsed.total_seconds()
            if hasattr(final_response, '_httpie_headers_parsed_at'):
                time_since_headers_parsed = monotonic() - final_response._httpie_headers_parsed_at
                total_time = time_to_parse_headers + time_since_headers_parsed
            else:
                total_time = time_to_parse_headers
            metadata['response']['total_time_seconds'] = round(total_time, 6)
        except Exception:
            pass

    return metadata


def _save_metadata_to_file(filepath: str, metadata: dict) -> None:
    filepath = os.path.abspath(filepath)
    records = []
    
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if content.strip():
                    records = json.loads(content)
                    if not isinstance(records, list):
                        records = [records]
        except (json.JSONDecodeError, IOError, OSError):
            records = []

    records.append(metadata)
    
    temp_fd, temp_path = tempfile.mkstemp(
        dir=os.path.dirname(filepath) or '.',
        prefix='.httpie_meta_',
        suffix='.tmp'
    )
    try:
        with os.fdopen(temp_fd, 'w', encoding='utf-8') as f:
            json.dump(records, f, indent=2, ensure_ascii=False, default=str)
        
        if os.path.exists(filepath):
            os.replace(temp_path, filepath)
        else:
            os.rename(temp_path, filepath)
    except Exception:
        if os.path.exists(temp_path):
            try:
                os.unlink(temp_path)
            except Exception:
                pass
        raise


def program(args: argparse.Namespace, env: Environment) -> ExitStatus:
    """
    The main program without error handling.

    """
    # TODO: Refactor and drastically simplify, especially so that the separator logic is elsewhere.
    exit_status = ExitStatus.SUCCESS
    downloader = None
    initial_request: Optional[requests.PreparedRequest] = None
    final_response: Optional[requests.Response] = None
    response_body_preview: Optional[bytes] = None
    processing_options = ProcessingOptions.from_raw_args(args)

    def separate():
        getattr(env.stdout, 'buffer', env.stdout).write(MESSAGE_SEPARATOR_BYTES)

    def request_body_read_callback(chunk: bytes):
        should_pipe_to_stdout = bool(
            # Request body output desired
            OUT_REQ_BODY in args.output_options
            # & not `.read()` already pre-request (e.g., for  compression)
            and initial_request
            # & non-EOF chunk
            and chunk
        )
        if should_pipe_to_stdout:
            return write_raw_data(
                env,
                chunk,
                processing_options=processing_options,
                headers=initial_request.headers
            )

    try:
        if args.download:
            args.follow = True  # --download implies --follow.
            downloader = Downloader(env, output_file=args.output_file, resume=args.download_resume)
            downloader.pre_request(args.headers)
        messages = collect_messages(env, args=args,
                                    request_body_read_callback=request_body_read_callback)
        force_separator = False
        prev_with_body = False

        # Process messages as they’re generated
        for message in messages:
            output_options = OutputOptions.from_message(message, args.output_options)

            do_write_body = output_options.body
            if prev_with_body and output_options.any() and (force_separator or not env.stdout_isatty):
                # Separate after a previous message with body, if needed. See test_tokens.py.
                separate()
            force_separator = False
            if output_options.kind is RequestsMessageKind.REQUEST:
                if not initial_request:
                    initial_request = message
                if output_options.body:
                    is_streamed_upload = not isinstance(message.body, (str, bytes))
                    do_write_body = not is_streamed_upload
                    force_separator = is_streamed_upload and env.stdout_isatty
            else:
                final_response = message
                if args.check_status or downloader:
                    exit_status = http_status_to_exit_status(http_status=message.status_code, follow=args.follow)
                    if exit_status != ExitStatus.SUCCESS and (not env.stdout_isatty or args.quiet == 1):
                        env.log_error(f'HTTP {message.raw.status} {message.raw.reason}', level=LogLevel.WARNING)
            
            extra_stream_kwargs = None
            if args.save_meta and not args.offline and output_options.kind is RequestsMessageKind.RESPONSE:
                def response_body_chunk_callback(chunk: bytes):
                    nonlocal response_body_preview
                    if response_body_preview is None:
                        response_body_preview = b''
                    if len(response_body_preview) < 1024:
                        remaining = 1024 - len(response_body_preview)
                        response_body_preview += chunk[:remaining]
                
                extra_stream_kwargs = {
                    'on_body_chunk_downloaded': response_body_chunk_callback
                }
            
            write_message(
                requests_message=message,
                env=env,
                output_options=output_options._replace(
                    body=do_write_body
                ),
                processing_options=processing_options,
                extra_stream_kwargs=extra_stream_kwargs
            )
            prev_with_body = output_options.body

        # Cleanup
        if force_separator:
            separate()
        if downloader and exit_status == ExitStatus.SUCCESS:
            # Last response body download.
            download_stream, download_to = downloader.start(
                initial_url=initial_request.url,
                final_response=final_response,
            )
            
            if args.save_meta and not args.offline:
                original_callback = download_stream.on_body_chunk_downloaded
                
                def download_chunk_callback(chunk: bytes):
                    nonlocal response_body_preview
                    if response_body_preview is None:
                        response_body_preview = b''
                    if len(response_body_preview) < 1024:
                        remaining = 1024 - len(response_body_preview)
                        response_body_preview += chunk[:remaining]
                    if original_callback:
                        original_callback(chunk)
                
                download_stream.on_body_chunk_downloaded = download_chunk_callback
            
            write_stream(stream=download_stream, outfile=download_to, flush=False)
            downloader.finish()
            if downloader.interrupted:
                exit_status = ExitStatus.ERROR
                env.log_error(
                    f'Incomplete download: size={downloader.status.total_size};'
                    f' downloaded={downloader.status.downloaded}'
                )

        if args.save_meta:
            metadata = _collect_metadata(
                initial_request=initial_request,
                final_response=final_response,
                response_body_preview=response_body_preview,
                args=args,
            )
            _save_metadata_to_file(args.save_meta, metadata)

        return exit_status

    finally:
        if downloader and not downloader.finished:
            downloader.failed()
        if args.output_file and args.output_file_specified:
            args.output_file.close()


def print_debug_info(env: Environment):
    env.stderr.writelines([
        f'HTTPie {httpie_version}\n',
        f'Requests {requests_version}\n',
        f'Pygments {pygments_version}\n',
        f'Python {sys.version}\n{sys.executable}\n',
        f'{platform.system()} {platform.release()}',
    ])
    env.stderr.write('\n\n')
    env.stderr.write(repr(env))
    env.stderr.write('\n\n')
    env.stderr.write(repr(plugin_manager))
    env.stderr.write('\n')


def decode_raw_args(
    args: List[Union[str, bytes]],
    stdin_encoding: str
) -> List[str]:
    """
    Convert all bytes args to str
    by decoding them using stdin encoding.

    """
    return [
        arg.decode(stdin_encoding)
        if type(arg) is bytes else arg
        for arg in args
    ]
