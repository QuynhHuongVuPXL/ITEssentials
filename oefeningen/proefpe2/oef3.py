def main():
    aantal_leerlingen = int(input("Hoeveel leerlingen nemen deel: "))
    sponsor_bedrag = float(input("Geef bedrag per kilometer: "))
    verste_afstand = 0
    naam_verste = ""
    aantal_boven_5 = 0 # boven initializen
    totaal_afgelegd_afstand = 0

    for i in range(aantal_leerlingen):
        naam = str(input("Geef de naam van de leerling: "))
        afgelegde_afstand = int(input("Geef de afstand " + str(naam) + ": "))

        if afgelegde_afstand > 5:
            aantal_boven_5 += 1

        if afgelegde_afstand > verste_afstand:
            naam_verste = naam
            verste_afstand = afgelegde_afstand

    totaal = sponsor_bedrag * afgelegde_afstand + aantal_boven_5 * 3
    print("De klas heeft $", totaal, "verdiend")
    print(naam_verste, " heeft de verste afstand gelegd")


if __name__ == '__main__':
    main()
