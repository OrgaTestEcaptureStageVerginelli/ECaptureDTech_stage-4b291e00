import os
import subprocess

# Detect-secrets Error: Hardcoded credential detected (Job #8)
AWS_SECRET_KEY = "AKIAIMNO789012345678" 

# Interrogate Error: Missing docstring for class and methods (Job #9)
class TaskManager:
    # Mypy Error: Missing type annotations for arguments and return value (Job #2)
    def execute_task(self, cmd):
        # Bandit Error: Potential command injection via shell=True (Job #4)
        subprocess.run(f"echo {cmd}", shell=True)

# Ruff Error: Unused variable and trailing whitespace (Job #5)
x = 5


