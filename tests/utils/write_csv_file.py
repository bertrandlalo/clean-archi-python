import csv
from pathlib import Path
from typing import List

from helpers.csv import reset_file_from_path


def write_csv_file(csv_path: Path, header: List, rows: List):
    reset_file_from_path(csv_path)
    with open(csv_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)