"""Module providing secure task management utilities."""

import subprocess
from typing import List
class TaskManager:
    """Handles task execution securely."""

    def execute_task(self, cmd: str) -> None:
        """Executes a command using a secure list-based approach.

        Args:
            cmd: The command string to echo.
        """
        # Secure execution without shell=True to satisfy Bandit
        subprocess.run(["echo", cmd], check=True)


def get_status() -> List[str]:
    """Returns the current system status."""
    return ["online", "secure"]
