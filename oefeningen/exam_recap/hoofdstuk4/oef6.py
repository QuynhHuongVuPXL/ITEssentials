totaal = 0
artikelnummer = int(input("Geef het artikelnummer in: "))

while artikelnummer != 999:
    eenheidsprijs = float(input("Geef het eenheidsprijs in: "))
    aantal = int(input("Geef het aantal in: "))

    bedrag = eenheidsprijs * aantal
    totaal += bedrag

    print("artikel nr = " + str(artikelnummer) + " / hoeveelheid = " + str(aantal) + " / eenheidsprijs = " + str(eenheidsprijs) + " bedrag = " + str(bedrag))

    artikelnummer = int(input("Geef het artikelnummer in: "))
print("Het totale bedrag van de aankoop is " + str(totaal))