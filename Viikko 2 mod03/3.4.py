
vuosiluku = int(input("Vuosiluku: "))
if vuosiluku %4 == 0 and vuosiluku < 100:
    print("Vuosiluku on karkausvuosi")
elif vuosiluku %100 == 0 and vuosiluku > 100 and vuosiluku %400 == 0:
        print("Vuosiluku on karkausvuosi")
else:
    print("Vuosiluku ei ole karkausvuosi")
