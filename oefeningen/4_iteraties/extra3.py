totaal_deelnemers = 0
geslaagd = 0

naam = str(input("Geef de naam van de manager in: "))
while naam != "xx" and naam != "XX":
    totaal = 0
    totaal_deelnemers += 1

    test1 = int(input("Test1: "))
    test2 = int(input("Test2: "))
    test3 = int(input("Test3: "))

    totaal += test1 + test2 + test3
    gemiddelde = totaal / 3

    if gemiddelde < 70:
        resultaat = "faalt"
    else:
        resultaat = "slaagt"
        geslaagd += 1

    print(
        f"{naam} Test1: {test1} Test2: {test2} Test3: {test3} Gemiddelde: {round(gemiddelde, 1)} Resultaat: {resultaat}")

    naam = str(input("Geef de naam van de manager in: "))

percentage_geslaagd = geslaagd / totaal_deelnemers * 100
print("Er slaagde", percentage_geslaagd, "% van de", totaal_deelnemers, "deelnemers")


