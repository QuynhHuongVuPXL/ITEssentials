aantal_deelnemers = 0
aantal_slechte_conditie = 0

geslacht = int(input("Geef het geslacht van de werknemer in (1 = vrouw / 2 = man): "))

while not (geslacht != 1 and geslacht != 2):
    aantal_deelnemers += 1
    afstand_in_km = float(input("Geef de afstand in km na 12 min lopen: "))

    afstand_in_meter = afstand_in_km * 1000

    conditie_getal = (afstand_in_meter - 504.9) / 44.73

    if (geslacht == 1 and conditie_getal < 29) or (geslacht == 2 and conditie_getal < 36):
        aantal_slechte_conditie += 1

    geslacht = int(input("Geef het geslacht van de werknemer in (1 = vrouw / 2 = man): "))

gemiddelde_percentage_slechte_conditie = aantal_slechte_conditie / aantal_deelnemers * 100
print("Het percentage werknemers met een slechte conditie is " + str(gemiddelde_percentage_slechte_conditie))
