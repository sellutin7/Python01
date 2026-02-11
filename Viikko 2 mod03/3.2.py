hyttiluokka = input("Valitse hyttiluokka (Lux, A, B, C): ")

if hyttiluokka == "Lux":
    print("Parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("Ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("Ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("Ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")
