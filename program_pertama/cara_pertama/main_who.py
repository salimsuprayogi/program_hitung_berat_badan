# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

print("=======================================================")

print("Hitung berat badan ideal orang WHO (BMI)")

print("=======================================================")
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

print("=======================================================")
print("Hasil hitung berat badan ideal BMI kamu :", hasil)
# cetak hasil berdasarkan rumus BMI WHO
print("=======================================================")

if hasil < 18.5:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Kamu termasuk kurus")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
elif (hasil >= 18.5 and hasil <= 24.9):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Kamu termasuk normal")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
elif (hasil >= 25 and hasil <= 29.9):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Kamu termasuk Overweight")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
elif hasil >= 30:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Kamu termasuk Obesitas")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
else:
    pass

print("=======================================================")
