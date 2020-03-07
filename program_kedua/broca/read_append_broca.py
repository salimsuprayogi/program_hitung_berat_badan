# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

import csv

print("==============================================")

print("Hitung berat badan ideal berdasarkan rumus broca")

print("==============================================")

print("menu \n Silahkan pilih (1/2) \n 1. Hitung berat badan \n 2. Data berat badan")

pilih = input("input : ")

cari = []
# perulangan menggunakan while untuk mencari input string 1 atau 2
# jika tidak ditemukan, maka akan di minta untuk onput terus sampai kondisi string 1 atau 2 ditemukan

while cari == []:
    if pilih == "1":
        # jika ditemukan variabel [pilih] sama dengan string 1, maka jalankan kondisi ini
        cari = "1"
        # print(cari)
    elif pilih == "2":
        # jika ditemukan variabel [pilih] sama dengan string 2, maka jalankan kondisi ini
        cari = "2"
        # print(cari)
    else:
        # jika ditemukan variabel [pilih] tidak ditemukan string 1 dan 2, maka jalankan kondisi ini
        print("angka saja")
        pilih = input("input : ")

    if cari != []:
        # jika variabel [cari] tidak sama dengan value kosong, maka pencarian di hentikan
        # jika tidak di berhentikan dengan [ tidak sama dengan ], maka akan perulangan terus menerus
        pass

if cari == "1":
    nama = input("Nama kamu siapa : ")
    jenisKelamin = input("Jenis kelamin kamu apa : ")

    statusJKM = ["laki-laki", "pria", "L", "l", "lelaki", "cowok"]
    statusJKW = ["wanita", "perempuan", "cewek", "P", "p"]

    if jenisKelamin in statusJKM:
        genderK = "Laki-Laki"
        # print(genderK)
        tbPria = input("Berapa tinggi badan kamu : ")
        
        print("==============================================")

        bbIdealPria = (int(tbPria) - 100) - (10 / 100 * (int(tbPria) - 100))
        
        print("Berat badan ideal kamu adalah : ", bbIdealPria, "kg")

        with open("./program_kedua/broca/data_user_broca.csv", "r") as readCSV:
            read_csv = csv.reader(readCSV, delimiter=",")
            
            header = [
                "Nama", "Jenis Kelamin", "Tinggi Badan", "BB Ideal"
            ]
            
            data = [
                {"Nama": nama, "Jenis Kelamin": genderK,
                    "Tinggi Badan": tbPria, "BB Ideal": bbIdealPria}
            ]
            
            with open("./program_kedua/broca/data_user_broca.csv", "a", newline="") as addCSV:
                addData = csv.DictWriter(
                    addCSV, delimiter=",", fieldnames=header
                )
                addData.writerows(data)

    if jenisKelamin in statusJKW:
        genderP = "Perempuan"
        # print("Perempuan")
        tbWanita = input("Berapa tinggi badan kamu : ")

        print("==============================================")

        bbIdealWanita = (int(tbWanita) - 100) - \
            (15 / 100 * (int(tbWanita) - 100))
        print("Berat badan ideal kamu adalah : ", bbIdealWanita, "kg")


        with open("./program_kedua/broca/data_user_broca.csv", "r") as readCSV:
            read_csv = csv.reader(readCSV, delimiter=",")
            header = [
                "Nama", "Jenis Kelamin", "Tinggi Badan", "BB Ideal"
            ]

            data = [
                {"Nama": nama, "Jenis Kelamin": genderP,
                    "Tinggi Badan": tbWanita, "BB Ideal": bbIdealWanita}
            ]

            with open("./program_kedua/broca/data_user_broca.csv", "a", newline="") as addCSV:
                addData = csv.DictWriter(
                    addCSV, delimiter=",", fieldnames=header
                )
                addData.writerows(data)

if cari == "2":
    with open("./program_kedua/broca/data_user_broca.csv", "r", newline="") as bacadata:
        judul = ["Nama", "Jenis Kelamin", "Tinggi Badan", "BB Ideal"]
        
        savedata = csv.DictReader(bacadata, delimiter=",", fieldnames=judul)
        
        cariNama = input("Nama Anda : ")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        for csvNama in savedata:
            if csvNama["Nama"] == cariNama:
                print("Data Kamu Adalah : \n", "1. Nama Kamu", csvNama["Nama"], "\n", "2. Jenis Kelamin Kamu", csvNama["Jenis Kelamin"], "\n",
                      "3. Tinggi Badan Kamu", csvNama["Tinggi Badan"], "\n", "4. Berat Badan Ideal Kamu", csvNama["BB Ideal"])
            else:
                pass

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

print("===================================s===========")

# oke, secara keseluruhan sudah sesuai target. next -> belajar Database MySQL
