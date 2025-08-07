import os
import logging

from pathlib import Path


def get_repo_root() -> Path:
    """
    Returns the root directory of the repository.
    
    :return: Path, root directory of the repository
    """
    
    start_path = Path.cwd()

    for path in [start_path] + list(start_path.parents):
        if (path / '.git').exists():
            return path
        
repo_root = get_repo_root()

data_root = repo_root / 'data'

if __name__ == "__main__":
    # Example usage
    root = get_repo_root()
    print(f"Repository root directory: {root}")

    print(f"Data root directory: {data_root}")







