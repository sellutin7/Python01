leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Muunnetaan kaikki luodeiksi

luodit_yht = leiviskat * 20 * 32 + naulat * + luodit

# Muunnetaan grammoiksi
grammat = luodit_yht * 13.3

#Erotellaan kokonaiset kilogrammat ja loput grammat

kilot = int(grammat // 1000)
grammat_jaljella = grammat % 1000

print(f"Massa on {kilot} kilogrammaa ja {grammat_jaljella:.2f} grammaa")
