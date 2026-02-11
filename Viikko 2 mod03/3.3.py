sukupuoli = input("Valitse (nainen, mies):")
hgarvo = int(input("Anna hemoglobiiniarvo (g/l):"))

if sukupuoli == "nainen":
    if hgarvo > 117:
        print("Hemoglobiiniarvo on alhainen")
    elif hgarvo < 175:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")
elif sukupuoli == "mies":
    if hgarvo > 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hgarvo < 195:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")
