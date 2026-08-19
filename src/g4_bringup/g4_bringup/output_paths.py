"""Portable output paths for the archived bringup package."""

import os
from pathlib import Path


def default_results_dir() -> str:
    """Return a user-writable default without depending on the launch CWD."""
    state_home = os.environ.get('XDG_STATE_HOME')
    configured_root = Path(state_home).expanduser() if state_home else None
    state_root = (
        configured_root
        if configured_root is not None and configured_root.is_absolute()
        else Path.home() / '.local' / 'state'
    )
    return str(state_root / 'geant4-gazebo-radiation-prototype' / 'results')
