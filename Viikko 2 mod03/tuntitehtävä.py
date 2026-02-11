luku = int(input("Anna kokonaisluku:"))
if luku > 0:
    print("Luvun itseisarvo:", luku)
elif luku < 0:
    neg = luku*-1
    print("Luvun itseisarvo:", neg)
else:
    print("Luvun itseisarvo:", luku)
