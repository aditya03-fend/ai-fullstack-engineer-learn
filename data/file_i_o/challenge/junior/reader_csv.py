from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent

csv_file = BASE_DIR / "student.csv"
txt_file = BASE_DIR / "student.txt"

with open(csv_file, "r") as f_csv:
    reader = csv.DictReader(f_csv)

    with open(txt_file, "w") as f_txt:
        for row in reader:
            nama = row["nama"]
            nilai = int(row["nilai"])

            status = "lulus" if nilai >= 75 else "tidak lulus"

            f_txt.write(f"{nama} {status}\n")

    print("sukses")
