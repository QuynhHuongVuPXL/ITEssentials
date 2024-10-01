getal1 = int(input("Geef getal 1 in: "))
getal2 = int(input("Geef getal 2 in: "))

if getal1 > getal2:
    grootste_getal = getal1
    kleinste_getal = getal2
else:
    grootste_getal = getal2
    kleinste_getal = getal1

kwadraat = kleinste_getal ** 2
deling = grootste_getal / kleinste_getal

print("het kleinste getal is " + str(kleinste_getal))
print("het kwadraat van het kleinste getal is " + str(kwadraat))
print("het grootste gedeeld door het kleinste is " + str(deling))
