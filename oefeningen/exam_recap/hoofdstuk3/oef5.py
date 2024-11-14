EENHEIDSPRIJS = 11.5
BTWPERCENTAGE = 1.21

stuks = int(input("Hoeveel stuks wil je? "))
totale_prijs = EENHEIDSPRIJS * stuks * BTWPERCENTAGE
if totale_prijs > 1000:
    totale_prijs *= 0.90

print("De totale prijs is " + str(totale_prijs))