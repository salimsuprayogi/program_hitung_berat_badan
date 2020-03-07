# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

import csv

header = ["Nama", "Berat Badan", "Tinggi Badan", "BB Ideal BMI", "Status"]

dataku = [
    {"Nama": [], "Jenis Kelamin": [], "Tinggi Badan": [], "BB Ideal":[], "Status":[]}
]

nama_csv = "./program_kedua/asia_pasific/data_user_asia.csv"

with open(nama_csv, "w", newline="") as dataBMI:
    writeCsv = csv.DictWriter(dataBMI, delimiter=",", fieldnames=header)
    writeCsv.writeheader()
