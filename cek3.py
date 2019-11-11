print("Hitung berat badan ideal menurut broca")
print("=================================================")

nama = input("Nama kamu siapa : ")
jenisKelamin = input("Jenis kelamin kamu : ")

"""
nama="h"(x)
- = snake_case
jeisKelamin = camelCase
tipe ejaan
print("a")
"""

statusJKM = ["laki-laki", "pria", "L", "l", "lelaki", "cowok"]
statusJKW = ["wanita", "perempuan", "cewek", "P", "p"]


def hitungBB(sts, jenis):
    # ketika mengunakan fungsi wajib menyertakan def, in, type (keyword) sama nama fungsinya (ex:hitungBB)
    # wajib di masuki 2 argumen, contoh (sts, jenis)
    if jenis == "bmi":
        r = (int(sts) - 100) - (10 / 100 * (int(sts) - 100))
        print("=================================================")
        print("Berat badan ideal kamu adalah : ", r, "kg")
    elif jenis == "bmiW":
        rm4 = (int(sts) - 100)-(15 / 100 * (int(sts) - 100))
        print("=================================================")
        print("Berat badan ideal kamu adalah : ", rm4, "kg")


for statusM in statusJKM:
    if statusM == jenisKelamin:
        statusM = input("Berapa tinggi badan kamu : ")  # dinamik / dinamis
        if statusM.isnumeric():
            hitungBB(statusM, "bmi")
        else:
            print("input harus berupa angka (contoh : 170)")

for statusW in statusJKW:
    if statusW == jenisKelamin:
        statusW = input("Berapa tinggi badan kamu : ")
        # print(statusW)
        hitungBB(statusW, "bmiW")
print("=================================================")
