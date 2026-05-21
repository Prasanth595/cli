# Troubleshooting

This guide covers common issues and error conditions you may encounter when using HTTPie.

## Collecting Debug Information

When reporting a bug, always include the full command and output. Use the `--debug` flag to get detailed diagnostics:

```bash
$ http --debug <COMPLETE ARGUMENT LIST>
<COMPLETE OUTPUT>
```

The `--debug` flag prints the full request, response headers, SSL handshake details, and environment information that maintainers need to diagnose your issue.

## Exit Status Codes

HTTPie uses specific exit codes to indicate the result of a request. Understanding them helps diagnose failures:

| Exit Code | Constant | Meaning |
|-----------|----------|---------|
| `0` | `SUCCESS` | Request succeeded |
| `1` | `ERROR` | General error (connection failure, parse error, etc.) |
| `2` | `ERROR_TIMEOUT` | Request timed out |
| `3` | `ERROR_HTTP_3XX` | Redirect (only when `--check-status` is set) |
| `4` | `ERROR_HTTP_4XX` | Client error response (4xx status) |
| `5` | `ERROR_HTTP_5XX` | Server error response (5xx status) |
| `6` | `ERROR_TOO_MANY_REDIRECTS` | Redirect loop detected |
| `7` | `PLUGIN_ERROR` | A plugin raised an error |
| `130` | `ERROR_CTRL_C` | Interrupted by Ctrl+C |

Use `http --check-status` to have HTTPie exit with a non-zero code when the server returns a 3xx/4xx/5xx response, which is useful in CI/CD pipelines.

## Connection Problems

### Connection Refused or Timeout

```
Error: Max retries exceeded with url: /foo
(Caused by NewConnectionError('<pip._vendor.urllib3.connection.HTTPConnection object at 0x...>:
Failed to establish a new connection: [Errno 111] Connection refused'))
```

**Causes:**
- The server is not running or not listening on the target host/port
- A firewall is blocking the connection
- The wrong port number in the URL

**Solutions:**
1. Verify the server is running: `curl http://localhost:8000/foo` (or whatever host you're targeting)
2. Check the URL has the correct scheme (`http` vs `https`), host, and port
3. If connecting to a remote server, confirm it's reachable from your machine: `ping <host>`
4. Try with `--timeout=30` to rule out very short timeouts on slow connections

### SSL/TLS Errors

#### Certificate Verify Failed

```
SSL_CERTIFICATE_ERROR: certificate verification failed
```

**Causes:**
- The server's SSL certificate is self-signed or signed by an unknown CA
- Corporate proxies intercept HTTPS traffic with their own certificates

**Solutions:**
1. For self-signed certificates, tell HTTPie to skip verification (dev only):
   ```bash
   http --verify=no https://self-signed.example.com/
   ```
2. For corporate proxies, point HTTPie at your organization's CA bundle:
   ```bash
   http --verify=/path/to/company-ca-bundle.crt https://example.com/
   ```
3. Set the `REQUESTS_CA_BUNDLE` environment variable to persist the CA bundle across invocations

#### SSL Version Mismatch

```
ssl.SSLError: sslv3 alert handshake failure
```

**Causes:**
- The server only supports older SSL/TLS versions disabled in your Python/OpenSSL build
- The server requires a specific TLS version (e.g., TLS 1.0 for legacy systems)

**Solutions:**
1. Request a specific SSL version:
   ```bash
   http --ssl=ssl3 https://legacy.example.com/   # SSLv3 (often required for legacy)
   http --ssl=tls1   https://legacy.example.com/  # TLS 1.0
   http --ssl=tls1.2 https://example.com/         # TLS 1.2 (modern default)
   ```
2. Available options: `ssl2.3`, `ssl3`, `tls1`, `tls1.1`, `tls1.2`, `tls1.3`

### Proxy Errors

#### Proxy Authentication Failed

```
HTTPProxyError: Proxy authentication required
```

**Solutions:**
1. Pass credentials via the `--proxy` flag:
   ```bash
   http --proxy=http://user:password@proxy.example.com:8080 https://example.com/
   ```
2. Set the `HTTP_PROXY` / `HTTPS_PROXY` environment variables:
   ```bash
   export HTTP_PROXY=http://user:password@proxy.example.com:8080
   http https://example.com/
   ```
3. For NTLM-proxied environments, consider using a tool like `cntlm` as a local proxy that handles NTLM auth

#### Tunnel Connection Error

```
ProxyError: HTTPSConnectionPool(host='proxy.example.com', port=8080):
Can't connect to proxy because ' tunnel connection requires SSL'
```

**Causes:**
- Misconfigured proxy URL (e.g., using `https://` for an HTTP proxy)
- Proxy only supports HTTP, not HTTPS tunneling

**Solution:** Use `http://` for the proxy URL:
```bash
http --proxy=http://proxy.example.com:8080 https://example.com/
```

## Request Errors

### Invalid JSON in Body

```
ParseError: Expecting value: line 1 column 1 (char 0)
```

**Causes:**
- Passing `--json` with data that isn't valid JSON
- Using shell variable expansion that produced empty or malformed JSON

**Solutions:**
1. Validate your JSON before sending:
   ```bash
   http --json='{"name": "value"}' https://example.com/api
   ```
2. For complex data, use a file: `http --json=@data.json https://example.com/api`
3. Check for shell quoting issues — single quotes prevent shell expansion:
   ```bash
   # Good
   http --json='{"key": "value with $pecial chars"}' https://example.com/
   # Bad — $pecial gets expanded by the shell
   http --json="{"key": "value with $pecial chars"}" https://example.com/
   ```

### Invalid HTTP Status Codes

HTTPie correctly handles all valid HTTP status codes (100–599). If you see a status code outside this range:

```
ValueError: invalid http status code: 999
```

This is a server-side issue — the remote server is returning an improperly formatted response. Report this to the server's maintainers. As a workaround, avoid following redirects to that endpoint or use `--offline` to build and inspect the request without sending it.

### Content-Encoding Gzip Errors (Downloads)

If you encounter `Incomplete download` errors when the server uses gzip Content-Encoding:

```
Error: Incomplete download: Content-Encoding: gzip
```

This is a known issue tracked in [#1843](https://github.com/httpie/cli/issues/1843) and [#1707](https://github.com/httpie/cli/issues/1707). The issue occurs when HTTPie doesn't correctly handle gzip-encoded responses during file downloads. Ensure you have the latest version of HTTPie, as fixes for this are included in newer releases.

## Authentication Errors

### Credentials Not Being Sent

```
HTTPieKeyError: key name is not defined: 'SECRET_TOKEN'
```

**Causes:**
- Auth value referenced in the command was not found in the environment
- Typo in the environment variable name

**Solutions:**
1. Check the environment variable is set: `echo $SECRET_TOKEN`
2. Export it before running HTTPie:
   ```bash
   export SECRET_TOKEN=your_token_here
   http https://example.com/ Authorization: Bearer:$SECRET_TOKEN
   ```
3. Use `--print=hH` to see what headers are actually being sent in the request

### SSL Client Certificate Auth Failures

```
SSL: SSLCertVerificationError: certificate verify failed: self-signed certificate in certificate chain
```

**Solution:** Provide a client certificate and optional key:
```bash
http --cert=client.crt --cert-key=client.key https://example.com/
```

For password-protected key files, use `--cert-key-password` or the `HTTPIE_CERT_KEY_PASSWORD` environment variable.

## Shell and Platform Issues

### Command Not Found After Installation

**On macOS**, `brew` installs HTTPie as `httpie` (not `http` which may conflict with system binaries). Use `httpie` instead of `http`, or create an alias: `alias http=httpie`.

**On Windows**, ensure the pip install directory is in your `PATH`. If using the Windows Store Python, restart your terminal after installation.

### Path Expansion Issues on Windows

On Windows, percent-encoded paths like `C:\Users\Name\file.json` may be incorrectly expanded by `cmd.exe`. Use PowerShell or double-quote carefully:

```powershell
# PowerShell
http --json="@C:\Users\Name\file.json" https://example.com/api
```

### Python Version Incompatibility

HTTPie requires Python 3.7 or later. If you see `SyntaxError` or import errors:

```bash
$ http --version
# python3: ImportError: cannot import name 'charset_normalizer' from 'requests'
```

**Solution:** Upgrade HTTPie and its dependencies:
```bash
python -m pip install --upgrade httpie
```

## Getting More Help

- Full documentation: <https://httpie.io/docs>
- Discord community: <https://httpie.io/discord>
- Twitter: [@httpie](https://twitter.com/httpie)
- StackOverflow: [tag httpie](https://stackoverflow.com/questions/tagged/httpie)
- GitHub Issues: <https://github.com/httpie/cli/issues> (bug reports and feature requests)

When opening a GitHub issue, include:
1. The full command you ran (including all arguments)
2. The complete output (use `http --debug` to get verbose output)
3. Your HTTPie version: `http --version`
4. Your Python version: `python --version`
5. Your operating system