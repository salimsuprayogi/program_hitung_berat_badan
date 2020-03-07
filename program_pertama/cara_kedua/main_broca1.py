# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

print("=======================================================")
print("Hitung berat badan ideal menurut broca")
print("=======================================================")

# input-an user
nama = input("Nama kamu siapa : ")
jenisKelamin = input("Jenis kelamin kamu apa : ")

# pilihan jenis kelamin user
statusJKM = ["laki-laki", "pria", "L", "l", "lelaki", "cowok"]
statusJKW = ["wanita", "perempuan", "cewek", "P", "p"]


def hitungBB(sts, jenis):
    """
    def = fungsi
    hitungBB = nama fungsi
    sta, jenis = parameter
    fungsi adalah pernyataan yg sudah pasti / rumus
    """
    print("=======================================================")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if jenis == "bmi":
        r = (int(sts) - 100)-(10 / 100 * (int(sts) - 100))
        print("Berat badan ideal kamu adalah : ", r, "kg")
    elif jenis == "bmiW":
        rm1 = int(statusW) - 100
        rm2 = 15 / 100
        rm3 = rm2 * (int(statusW) - 100)
        rm4 = rm1 - rm3
        print("Berat badan ideal kamu adalah : ", rm4, "kg")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


for statusM in statusJKM:
    if statusM == jenisKelamin:
        statusM = input("Berapa tinggi badan kamu : ")
        if statusM.isnumeric():
            hitungBB(statusM, "bmi")
            # rumus diambil menggunakan fungsi (def)
            # isnumeric() untuk mencari input berupa int
        else:
            print("input harus berupa angka (contoh : 170)")
            # jika input berupa string (alphabet : abcde) -> else yang akan di jalankan
for statusW in statusJKW:
    if statusW == jenisKelamin:
        statusW = input("Berapa tinggi badan kamu : ")
        hitungBB(statusW, "bmiW")

print("=======================================================")
