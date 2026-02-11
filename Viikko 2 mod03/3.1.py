pituus = int(input("Anna kuhan pituus sentteinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Kuha on liian pieni, laske takaisin järveen")
    print("Pituutta puutuu ", puuttuu)
elif pituus >= 37:
    print("Kuha on tarpeeks iso, saat pitää!")
