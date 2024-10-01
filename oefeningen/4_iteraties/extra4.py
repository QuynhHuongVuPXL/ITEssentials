totaal_werknemers = 0
slechte_conditie = 0

geslacht = int(input("Geef het geslacht van de werknemer in (1 = vrouw / 2 = man): "))

while not (geslacht != 1 and geslacht != 2):
    totaal_werknemers += 1

    afstand_in_km = float(input("Geef de afstand in km na 12 min lopen: "))

    afstand_in_m = afstand_in_km * 1000
    conditie_getal = (afstand_in_m - 504.9) / 44.73

    if geslacht == 1 and conditie_getal < 29:
        slechte_conditie += 1
    elif geslacht == 2 and conditie_getal < 36:
        slechte_conditie += 1

    geslacht = int(input("Geef het geslacht van de werknemer in (1 = vrouw / 2 = man): "))

percentage_slechte_conditie = slechte_conditie / totaal_werknemers * 100
print("Het percentage werknemers met een slechte conditie is", percentage_slechte_conditie)
