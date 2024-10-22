def bereken_kinderbijslag(kind_nummer, leeftijd, code):
    basisbedrag = 0
    if code == "H":
        basisbedrag = 300
    else:
        basisbedrag = 75 + (kind_nummer - 1) * 70

    if leeftijd >= 12:
        basisbedrag += 25
    if leeftijd >= 6:
        basisbedrag += 25

    return basisbedrag


def main():
    totaal_bedrag = 0
    aantal_kinderen = int(input("Geef het aantal kinderen in: "))

    for kind_nummer in range(1, aantal_kinderen + 1):
        leeftijd = int(input("Geef de leeftijd in: "))
        code = str(input("Geef de code in: "))

        basisbedrag = bereken_kinderbijslag(kind_nummer, leeftijd, code)
        totaal_bedrag += basisbedrag

    print("De totale kinderbijslag bedraagt", totaal_bedrag)


if __name__ == '__main__':
    main()
