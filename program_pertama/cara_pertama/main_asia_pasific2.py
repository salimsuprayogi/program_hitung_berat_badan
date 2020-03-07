# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

# cara penulisan rumus yang berbeda
# hitung berat badan ideal dengan rumus BMI

print("=======================================================")

print("Hitung berat badan ideal orang Asia-Pasific (BMI)")

print("=======================================================")

bb = input("Berapa berat badan kamu : ")
tb = input("Berapa tinggi badan kamu : ")

"""
# rumus
rumusTb = float(tb) / 100
kuadrat_tb = (rumusTb ** 2)
hasil = int(bb) / kuadrat_tb
"""

# rumus
hasil = int(bb) / ((float(tb) / 100) ** 2)

print("=======================================================")
print("Hasil hitung berat badan ideal BMI kamu :", hasil)
print("=======================================================")

# pengkondisian
if hasil < 18.5:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Kamu termasuk kurus")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
elif (hasil >= 18.5 and hasil <= 22.9):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Kamu termasuk normal")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
elif (hasil >= 23 and hasil <= 24.9):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Kamu termasuk Overweight")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
elif hasil >= 25:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Kamu termasuk Obesitas")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
else:
    pass
print("=======================================================")
