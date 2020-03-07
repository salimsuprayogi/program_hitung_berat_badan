# Mentor = Muhammad Nasrullah
# Author = Salim Suprayogi

def hitungBB(sts, jenis):
    if jenis == "bmi":
        r = (int(sts) - 100) - (10 / 100 * (int(sts) - 100))
        print("Berat badan ideal kamu adalah : ", r, "kg")
    elif jenis == "bmiW":
        r = (int(sts)- 100)-(15 / 100 *(int(sts) - 100))
        print("Berat badan ideal kamu adalah : ", r, "kg")