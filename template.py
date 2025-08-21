import os
from pathlib import Path

# List of files you want to track/create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string to Path object
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create empty file if it doesn't exist
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass
        print(f"Created: {filepath}")
    else:
        print(f"Already exists: {filepath}")
