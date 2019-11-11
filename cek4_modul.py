def hitungBB(sts, jenis):
    if jenis == "bmi":
        r = (int(sts) - 100) - (10 / 100 * (int(sts) - 100))
        print("\n")
        print("Berat badan ideal kamu adalah : ", r, "kg")
    elif jenis == "bmiW":
        rm4 = (int(sts)- 100)-(15 / 100 *(int(sts) - 100))
        print("\n")
        print("Berat badan ideal kamu adalah : ", rm4, "kg")