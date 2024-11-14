aantal_examens = 3
totaal_managers = 0
totaal_geslaagd = 0
naam_manager = str(input("Geef de naam van de manager in: "))
while naam_manager != "XX" and naam_manager != "xx":
    totaal_managers += 1

    test1 = int(input("Test: "))
    test2 = int(input("Test: "))
    test3 = int(input("Test: "))

    gemiddelde = (test1 + test2 + test3) / aantal_examens

    if gemiddelde < 70:
        resultaat = "faalt"
    else:
        resultaat = "slaagt"
        totaal_geslaagd += 1

    print(
        f"{naam_manager} Test1: {test1} Test2: {test2} Test3: {test3} Gemiddelde: {round(gemiddelde, 1)} Resultaat: {resultaat}")

    naam_manager = str(input("Geef de naam van de manager in: "))

gemiddelde_geslaagd = totaal_geslaagd / totaal_managers * 100
print(f"Er slaagde {round(gemiddelde_geslaagd, 1)} % van de {totaal_managers} deelnemers")