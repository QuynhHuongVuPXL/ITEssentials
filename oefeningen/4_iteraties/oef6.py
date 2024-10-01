totaal = 0

artikelnummer = int(input("Geef artikelnummer in: "))

while artikelnummer != 999:
    eenheidsprijs = float(input("Geef eenheidsprijs in: "))
    aantal = int(input("Geef aantal in: "))

    bedrag = eenheidsprijs * aantal
    totaal += bedrag

    print(f"arikel nr {artikelnummer} / hoeveelheid = {aantal} / eenheidsprijs = {eenheidsprijs} / bedrag = {bedrag}")

    artikelnummer = int(input("Geef artikelnummer in: "))

print("Het totale bedrag van de aankoop is", totaal)
