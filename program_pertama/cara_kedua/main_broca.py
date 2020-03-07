# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

from broca import hitungBB as rumus

print("=======================================================")
nama = input("Nama kamu siapa : ")
jenisKelamin = input("Jenis kelamin kamu apa : ")

statusJKM = ["laki-laki", "pria", "L", "l", "lelaki", "cowok"]
statusJKW = ["wanita", "perempuan", "cewek", "P", "p"]


for statusM in statusJKM:
    if statusM == jenisKelamin:
        statusM = input("Berapa tinggi badan kamu : ")
        print("=======================================================")
        if statusM.isnumeric():
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            rumus(statusM, "bmi")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        else:
            print("input harus berupa angka (contoh : 170)")

for statusW in statusJKW:
    if statusW == jenisKelamin:
        statusW = input("Berapa tinggi badan kamu : ")
        print("=======================================================")
        if statusW.isnumeric():
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            rumus(statusW, "bmiW")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        else:
            print("input harus berupa angka (contoh : 170)")

print("=======================================================")
