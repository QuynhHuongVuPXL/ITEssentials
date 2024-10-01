eenheidsprijs = 11.5
BTW = 1.21

stuks = int(input("Hoeveel stuks wil je? "))

totale_prijs = (eenheidsprijs * stuks) * BTW

if totale_prijs > 1000:
    totale_prijs *= 0.90

print("De totale prijs is " + str(totale_prijs))
