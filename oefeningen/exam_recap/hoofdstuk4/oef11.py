man_ouder_dan_34_of_man_loon_hoger_1800 = 0
vrouw_jonger_dan_25 = 0

personeelsnummer = int(input("Geef jouw personeelsnummer in: "))
while personeelsnummer != 0:
    geslacht = int(input("Geef jouw geslacht in (0 = vrouw, 1 = man): "))

    while geslacht != 0 and geslacht != 1:
        geslacht = int(input("Foutief geslacht: geef opnieuw in (0 = vrouw, 1 = man): "))

    leeftijd = int(input("Geef jouw leeftijd in: "))
    brutoloon = int(input("Geef jouw brutoloon in: "))

    if (geslacht == 1 and leeftijd > 34) or (geslacht == 1 and brutoloon >= 1800):
        man_ouder_dan_34_of_man_loon_hoger_1800 += 1

    if geslacht == 0 and leeftijd < 25:
        vrouw_jonger_dan_25 += 1

    personeelsnummer = int(input("Geef jouw personeelsnummer in: "))
print("Het aantal mannen dat aan de voorwaarde voldoet is " + str(man_ouder_dan_34_of_man_loon_hoger_1800))
print("Het aantal vrouwen dat aan de voorwaarde voldoet is " + str(vrouw_jonger_dan_25))