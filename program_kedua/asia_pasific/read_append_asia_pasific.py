# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

import csv

print("==============================================")

print("Hitung berat badan ideal orang Asia-Pasific (BMI)")

print("==============================================")

print("menu \n Silahkan pilih (1/2) \n 1. Hitung berat badan \n 2. Data berat badan")

pilih = input("input : ")

cari = []

while cari == []:
    if pilih == "1":
        cari = "1"
        # print(cari)
    elif pilih == "2":
        cari = "2"
        # print(cari)
    else:
        print("angka saja")
        pilih = input("input : ")

    if cari != []:
        pass

if cari == "1":
    nama = input("Nama : ")

    bb = input("Berapa berat badan anda : ")
    # input berat badan
    bbKonversi = int(bb)
    # ubah data dari string ke integer
    # print(type(bbKonversi))

    tb = input("Berapa tinggi badan anda : ")
    # input tinggi badan
    tbKonversi = float(tb)
    # ubah data dari string ke float

    rumusTb = tbKonversi / 100
    # ubah data tinggi badan menjadi (cm)
    kuadrat_tb = (rumusTb ** 2)
    # mencari pangkat dari tinggi badan
    hasil = bbKonversi / kuadrat_tb
    # mencari hasil berat badan ideal dengan rumus BMI untuk Asia Pasifik

    print("==============================================")

    print("Hasil hitung berat badan ideal BMI kamu :", hasil)
    # cetak hasil berdasarkan rumus BMI Asia Pasifik

    with open("./program_kedua/asia_pasific/data_user_asia.csv", "r") as readCSV:
        readCsv = csv.reader(readCSV, delimiter=",")

    if hasil < 18.5:
        a = "Kamu termasuk kurus"

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        print("Kamu termasuk kurus")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        header = [
            "Nama", "Berat Badan", "Tinggi Badan", "BB Ideal BMI", "Status"
        ]

        dataku = [
            {"Nama": nama, "Berat Badan": bb, "Tinggi Badan": tb,
                "BB Ideal BMI": hasil, "Status": a}
        ]

        with open("./program_kedua/asia_pasific/data_user_asia.csv", "a", newline="") as addCSV:
            addCsv = csv.DictWriter(
                addCSV, delimiter=",", fieldnames=header
            )
            addCsv.writerows(dataku)

    elif (hasil >= 18.5 and hasil <= 22.9):
        b = "Kamu termasuk normal"

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        print("Kamu termasuk normal")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        header = [
            "Nama", "Berat Badan", "Tinggi Badan", "BB Ideal BMI", "Status"
        ]

        dataku = [
            {"Nama": nama, "Berat Badan": bb, "Tinggi Badan": tb,
                "BB Ideal BMI": hasil, "Status": b}
        ]

        with open("./program_kedua/asia_pasific/data_user_asia.csv", "a", newline="") as addCSV:
            addCsv = csv.DictWriter(
                addCSV, delimiter=",", fieldnames=header
            )
            addCsv.writerows(dataku)

    elif (hasil >= 23 and hasil <= 24.9):
        c = "Kamu termasuk Overweight"

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        print("Kamu termasuk Overweight")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        header = [
            "Nama", "Berat Badan", "Tinggi Badan", "BB Ideal BMI", "Status"
        ]

        dataku = [
            {"Nama": nama, "Berat Badan": bb, "Tinggi Badan": tb,
                "BB Ideal BMI": hasil, "Status": c}
        ]

        with open("./program_kedua/asia_pasific/data_user_asia.csv", "a", newline="") as addCSV:
            addCsv = csv.DictWriter(
                addCSV, delimiter=",", fieldnames=header
            )
            addCsv.writerows(dataku)

    elif hasil >= 25:
        d = "Kamu termasuk Obesitas"

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        print("Kamu termasuk Obesitas")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        header = [
            "Nama", "Berat Badan", "Tinggi Badan", "BB Ideal BMI", "Status"
        ]

        dataku = [
            {"Nama": nama, "Berat Badan": bb, "Tinggi Badan": tb,
                "BB Ideal BMI": hasil, "Status": d}
        ]

        with open("./program_kedua/asia_pasific/data_user_asia.csv", "a", newline="") as addCSV:
            addCsv = csv.DictWriter(
                addCSV, delimiter=",", fieldnames=header
            )
            addCsv.writerows(dataku)

    else:
        pass

# menampilkan data dari csv berdasarkan nama
# print("==============================================")
if cari == "2":
    with open("./program_kedua/asia_pasific/data_user_asia.csv", "r", newline="") as bacadata:
        judul = ["Nama", "Berat Badan",
                 "Tinggi Badan", "BB Ideal BMI", "Status"]
        
        savedata = csv.DictReader(bacadata, delimiter=",", fieldnames=judul)
        
        cariNama = input("Nama Anda : ")
        
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
        for csvNama in savedata:
            if csvNama["Nama"] == cariNama:
                print("Data Kamu Adalah : \n", "1. Nama Anda = ", csvNama["Nama"], "\n", "2. Berat Badan Anda = ", csvNama["Berat Badan"], "\n",
                      "3. Tinggi Badan Anda = ", csvNama["Tinggi Badan"], "\n", "4. Hasil hitung berat badan = ", csvNama["BB Ideal BMI"], "\n", "5. Status Anda = ", csvNama["Status"])
            else:
                pass
        
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

print("==============================================")
