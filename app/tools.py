from pathlib import Path
import platform
import sys

def run_safe_action(plan: str):
    """Allowlisted, non-destructive demo action.

    This intentionally does NOT execute arbitrary model-generated shell commands.
    """
    info = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "cwd": str(Path.cwd()),
    }
    return {
        "message": "✅ Human-approved demo tool executed. No arbitrary command was run.",
        "output": "\n".join(f"{k}: {v}" for k, v in info.items()),
    }
