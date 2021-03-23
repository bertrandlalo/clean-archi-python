import csv
from pathlib import Path
from src.helpers.csv import reset_file_from_path

csv_path = Path("tests/integration/data") / "user_repo.csv"


def test_can_add_user():
    reset_file_from_path(csv_path)
    # TODO


def test_can_get_user_if_exists():
    reset_file_from_path(csv_path)
    # TODO
