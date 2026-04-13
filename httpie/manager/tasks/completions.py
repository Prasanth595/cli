import os
import shutil
import sys
from pathlib import Path
from typing import Optional

from httpie.context import Environment
from httpie.status import ExitStatus


# Shell-specific completion directories
COMPLETION_DIRS = {
    'fish': [
        Path('/usr/share/fish/vendor_completions.d'),
        Path.home() / '.config/fish/completions',
    ],
    'bash': [
        Path('/etc/bash_completion.d'),
        Path.home() / '.local/share/bash-completion/completions',
    ],
    'zsh': [
        Path('/usr/local/share/zsh/site-functions'),
        Path.home() / '.zsh/completions',
    ],
}

# Map shell names to completion file names in extras/
COMPLETION_FILES = {
    'fish': 'httpie-completion.fish',
    'bash': 'httpie-completion.bash',
}


def get_completion_file(shell: str) -> Optional[Path]:
    """Get the path to the completion file for the given shell."""
    # extras/ is at the repo root, not inside httpie/
    extras_dir = Path(__file__).parent.parent.parent.parent / 'extras'
    filename = COMPLETION_FILES.get(shell)
    if filename:
        path = extras_dir / filename
        if path.exists():
            return path
    return None


def get_install_dir(shell: str) -> Optional[Path]:
    """Find the first writable completion directory for the shell."""
    for directory in COMPLETION_DIRS.get(shell, []):
        if directory.exists() and os.access(directory, os.W_OK):
            return directory
        # Try to create user directory if it doesn't exist
        if not directory.is_absolute() or str(directory).startswith(str(Path.home())):
            try:
                directory.mkdir(parents=True, exist_ok=True)
                if os.access(directory, os.W_OK):
                    return directory
            except (OSError, PermissionError):
                continue
    return None


def install_completions(shell: str, env: Environment) -> ExitStatus:
    """Install shell completions for the given shell."""
    completion_file = get_completion_file(shell)
    if not completion_file:
        env.stderr.write(f'No completion file found for shell: {shell}\n')
        env.stderr.write(f'Supported shells: {", ".join(COMPLETION_FILES.keys())}\n')
        return ExitStatus.ERROR

    install_dir = get_install_dir(shell)
    if not install_dir:
        env.stderr.write(f'Could not find a writable completion directory for {shell}.\n')
        env.stderr.write(f'Tried: {", ".join(str(d) for d in COMPLETION_DIRS.get(shell, []))}\n')
        env.stderr.write(f'You can manually copy {completion_file} to your completions directory.\n')
        return ExitStatus.ERROR

    # Determine target filename
    if shell == 'fish':
        target_name = 'http.fish'
    elif shell == 'bash':
        target_name = 'httpie'
    else:
        target_name = f'httpie.{shell}'

    target_path = install_dir / target_name

    try:
        shutil.copy2(completion_file, target_path)
        env.stdout.write(f'Installed {shell} completions to: {target_path}\n')
        if shell == 'fish':
            env.stdout.write('Completions will be available in new fish sessions.\n')
        elif shell == 'bash':
            env.stdout.write(f'Run `source {target_path}` or start a new session.\n')
        elif shell == 'zsh':
            env.stdout.write(f'Add `fpath=({install_dir} $fpath)` to your .zshrc and restart.\n')
        return ExitStatus.SUCCESS
    except (OSError, PermissionError) as e:
        env.stderr.write(f'Failed to install completions: {e}\n')
        env.stderr.write(f'Try running with sudo for system-wide installation.\n')
        return ExitStatus.ERROR


def cli_completions(env: Environment, args) -> ExitStatus:
    """Handle the completions subcommand."""
    shell = getattr(args, 'shell', None)
    action = getattr(args, 'completions_action', None)

    if action == 'install':
        if shell:
            return install_completions(shell, env)
        else:
            # Auto-detect and install for all supported shells
            detected_shells = []
            current_shell = os.path.basename(os.environ.get('SHELL', ''))
            if current_shell in COMPLETION_FILES:
                detected_shells.append(current_shell)

            if not detected_shells:
                env.stderr.write('Could not detect shell. Specify one: fish, bash, zsh\n')
                return ExitStatus.ERROR

            for s in detected_shells:
                result = install_completions(s, env)
                if result != ExitStatus.SUCCESS:
                    return result
            return ExitStatus.SUCCESS

    elif action == 'list':
        env.stdout.write('Available shell completions:\n')
        for shell, filename in COMPLETION_FILES.items():
            completion_file = get_completion_file(shell)
            status = 'available' if completion_file else 'not found'
            env.stdout.write(f'  {shell}: {status}\n')
        return ExitStatus.SUCCESS

    env.stderr.write('Please specify an action: install, list\n')
    return ExitStatus.ERROR
