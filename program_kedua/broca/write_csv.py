# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

import csv

judul = ["Nama", "Jenis Kelamin", "Tinggi Badan", "BB Ideal"]

dataku = [
    {"Nama": [], "Jenis Kelamin": [], "Tinggi Badan": [], "BB Ideal":[]}
]

nama_csv = "./program_kedua/broca/data_user_broca.csv"

with open(nama_csv, "w", newline="") as dataCsv:
    writeCsv = csv.DictWriter(dataCsv, delimiter=",", fieldnames=judul)
    writeCsv.writeheader()
