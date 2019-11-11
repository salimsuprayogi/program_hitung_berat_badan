import cek4_modul
# ambil untuk file yang bernama cek4_modul
# fungsi (from) untuk mengambil folder yang berbedda (program)
# 30 fungsi saling membutuhkan
# main = fungsi yang pertama kali di jalankan

nama = input("Nama kamu siapa : ")
jenisKelamin = input("Jenis kelamin kamu apa : ")

statusJKM = ["laki-laki", "pria", "L", "l", "lelaki", "cowok"]
statusJKW = ["wanita", "perempuan", "cewek", "P", "p"]

for statusM in statusJKM:
    if statusM == jenisKelamin:
        statusM = input("Berapa tinggi badan kamu : ")  # dinamik / dinamis
        if statusM.isnumeric():
            cek4_modul.hitungBB(statusM, "bmi")
            # print berat badan untuk pria
        else:
            print("input harus berupa angka (contoh : 170)")

for statusW in statusJKW:
    if statusW == jenisKelamin:
        statusW = input("Berapa tinggi badan kamu : ")
        if statusW.isnumeric():
            cek4_modul.hitungBB(statusW, "bmiW")
            # print berat badan ideal untuk wanita
        else:
            print("input harus berupa angka (contoh : 170)")

print("=================================================")

"""
Gambaran untuk menggunakan modul

a = SIMPEL DATANYA dinamiS (MAIN)
-->1 (MODUL)
    -->234 DATA STATIS(FUNGSI)
-->2
    -->456
-->3
    -->678
"""
