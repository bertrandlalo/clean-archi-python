from pathlib import Path 

def reset_file_from_path(path: Path):
    try:
        path.unlink()
    except FileNotFoundError:
        pass