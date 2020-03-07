# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

print("=======================================================")

print("Hitung berat badan ideal menurut broca")

print("=======================================================")

# input-an user
nama = input("Nama kamu siapa : ")
jenisKelamin = input("Jenis kelamin kamu : ")

# pilihan jenis kelamin user
statusJKM = ["laki-laki", "pria", "L", "l", "lelaki", "cowok"]
statusJKW = ["wanita", "perempuan", "cewek", "P", "p"]


def hitungBB(sts, jenis):
    """
    ketika mengunakan fungsi wajib menyertakan def

    (in, type (keyword) sama nama fungsi bawaan python (ex:hitungBB))

    wajib di masuki 2 argument, contoh (sts, jenis)
    """

    print("=======================================================")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if jenis == "bmi":
        r = (int(sts) - 100) - (10 / 100 * (int(sts) - 100))
        print("Berat badan ideal kamu adalah : ", r, "kg")
    elif jenis == "bmiW":
        rm4 = (int(sts) - 100)-(15 / 100 * (int(sts) - 100))
        print("Berat badan ideal kamu adalah : ", rm4, "kg")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


for statusM in statusJKM:
    if statusM == jenisKelamin:
        statusM = input("Berapa tinggi badan kamu : ")
        if statusM.isnumeric():
            hitungBB(statusM, "bmi")
        else:
            print("input harus berupa angka (contoh : 170)")

for statusW in statusJKW:
    if statusW == jenisKelamin:
        statusW = input("Berapa tinggi badan kamu : ")
        hitungBB(statusW, "bmiW")

print("=======================================================")
