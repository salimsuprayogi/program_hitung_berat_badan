print("Hitung berat badan ideal wanita berdasarkan rumus broca")
print("=======================================================")

tb = input("Berapa tinggi badan kamu :")

rms1 = int(tb) - 100
rms2 = 15 / 100
rms3 = rms2 * (int(tb) - 100)
rms4 = rms1 - rms3

print("Berat badan ideal kamu adalah : ", rms4, "kg")
print("=======================================================")
