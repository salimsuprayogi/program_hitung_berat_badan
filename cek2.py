print("Hitung berat badan ideal menurut broca")
print("=================================================")

nama = input("Nama kamu siapa : ")
jenisKelamin = input("Jenis kelamin kamu apa : ")

statusJKM = ["laki-laki", "pria", "L", "l", "lelaki", "cowok"]
statusJKW = ["wanita", "perempuan", "cewek", "P", "p"]


def hitungBB(sts, jenis):
    # def = fungsi
    # hitungBB = nama fungsi
    #sts, jenis = parameter
    if jenis == "bmi":
        r = (int(sts) - 100)-(10 / 100 * (int(sts) - 100))
        print("=================================================")
        print("Berat badan ideal kamu adalah : ", r, "kg")
    elif jenis == "bmiW":
        rm1 = int(statusW) - 100
        rm2 = 15 / 100
        rm3 = rm2 * (int(statusW) - 100)
        rm4 = rm1 - rm3
        print("=================================================")
        print("Berat badan ideal kamu adalah : ", rm4, "kg")
# menggunakan fungsi
#rumus = 1 + 2
#rumus2 = 3 - 3
#sts : paramater
#hitungBB = fungsi


for statusM in statusJKM:
    if statusM == jenisKelamin:
        statusM = input("Berapa tinggi badan kamu : ")
        if statusM.isnumeric():
            hitungBB(statusM, "bmi")
            #r = (int(statusM) - 100)-(10 / 100 *(int(statusM) - 100))
            #print("Berat badan ideal kamu adalah : ", r, "kg")
            # menuju fungsi
            # if: #gawe/menggunakan modul
            # fungsi: pernyataan yg sudah pasti / rumus
            # isnumeric() untuk mencari input berupa integer
            # rumus diambil menggunakan fungsi (def)
        else:
            print("input harus berupa angka (contoh : 170)")
            # jika input berupa string (alphabet : abcde) -> else yang akan di jalankan
            #print("Berat badan ideal kamu adalah : ", rms4, "kg")
        # print(statusM)

        """
        rms1 = int(statusM) - 100
        rms2 = 10 / 100
        rms3 = rms2 * (int(statusM) - 100)
        rms4 = rms1 - rms3
        else:
            r = (int(statusM) - 100)-(10 / 100 *(int(statusM) - 100))
            print("Berat badan ideal kamu adalah : ", r, "kg")
            #print("Berat badan ideal kamu adalah : ", rms4, "kg")
        """
for statusW in statusJKW:
    if statusW == jenisKelamin:
        statusW = input("Berapa tinggi badan kamu : ")
        # print(statusW)
        hitungBB(statusW, "bmiW")
print("=================================================")
