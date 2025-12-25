# membaca csv
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Membaca CSV sebagai Dictionary
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# menulis csv
import csv

data = [
    {"id": 1, "nama": "Doni", "umur": 35},
    {"id": 2, "nama": "Eka", "umur": 29}
]

with open("output.csv", "w", newline="") as file:
    fieldnames = ["id", "nama", "umur"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)
