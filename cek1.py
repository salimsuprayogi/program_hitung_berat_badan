# lanjutan dari 1, 2, 3 dan 4
# hitung berat badan ideal dengan rumus BMI

print("Hitung berat badan ideal orang Asia-Pasific (BMI)")
print("=================================================")

bb = input("Berapa berat badan kamu : ")
tb = input("Berapa tinggi badan kamu : ")

"""
rumusTb = float(tb) / 100
kuadrat_tb = (rumusTb ** 2)
hasil = int(bb) / kuadrat_tb
#rumus 2
"""

hasil = int(bb) / ((float(tb) / 100) ** 2)
# rumus 3

print("=================================================")
print("Hasil hitung berat badan ideal BMI kamu :", hasil)

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
# pengkondisian
