""" Configuration file for the project. """

from pathlib import Path
import os

MAX_DISPLAY_SIZE: int = 300_000
TMP_BASE_PATH = Path("/tmp/gitingest")
DELETE_REPO_AFTER: int = 60 * 60  # In seconds

EXAMPLE_REPOS: list[dict[str, str]] = [
    {"name": "Gitingest", "url": "https://github.com/cyclotruc/gitingest"},
    {"name": "FastAPI", "url": "https://github.com/tiangolo/fastapi"},
    {"name": "Flask", "url": "https://github.com/pallets/flask"},
    {"name": "Tldraw", "url": "https://github.com/tldraw/tldraw"},
    {"name": "ApiAnalytics", "url": "https://github.com/tom-draper/api-analytics"},
]

# Git clone timeout in seconds (default: 5 minutes)
CLONE_TIMEOUT = int(os.getenv("GITINGEST_CLONE_TIMEOUT", 300))

# Overall request timeout in seconds (default: 10 minutes) 
REQUEST_TIMEOUT = int(os.getenv("GITINGEST_REQUEST_TIMEOUT", 600))

# File processing timeout in seconds (default: 8 minutes)
PROCESSING_TIMEOUT = int(os.getenv("GITINGEST_PROCESSING_TIMEOUT", 480))
