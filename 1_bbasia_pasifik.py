#bb = 60
#tb = 1.70
print("Hitung berat badan ideal orang Asia-Pasific (BMI)")
print("==============================================")

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

if hasil < 18.5:
    print("Kamu termasuk kurus")
elif (hasil >= 18.5 and hasil <= 22.9):
    print("Kamu termasuk normal")
elif (hasil >= 23 and hasil <= 24.9):
    print("Kamu termasuk Overweight")
elif hasil >= 25:
    print("Kamu termasuk Obesitas")
else:
    pass
    # sama dengan (break)
# pengkondisian
