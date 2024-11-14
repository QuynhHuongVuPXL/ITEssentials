def bereken_kostprijs(oppervlakte):
    uren = oppervlakte / 160
    uren = int(uren) + 1
    kostprijs = uren * 12.5
    return kostprijs


def bereken_aantal_personen_en_uren(oppervlakte):
    totale_uren = oppervlakte / 160

    totaal_personen = int(totale_uren // 8)
    uren_werk = totale_uren % 8

    if totaal_personen > 0 and uren_werk > 0:
        return f"{totaal_personen} personen werken 8 uur\n1 persoon werkt {uren_werk} uur"
    elif totaal_personen > 0:
        return f"{totaal_personen} personen werken 8 uur"
    else:
        return f"1 persoon werkt {uren_werk} uur"


def main():
    oppervlakte = float(input("Geef het aantal m2 dat gekuist moet worden: "))
    while oppervlakte != 0:
        kostprijs = bereken_kostprijs(oppervlakte)
        print("Het kuisten van deze oppervlakte kost", kostprijs, "euro")

        print(bereken_aantal_personen_en_uren(oppervlakte))

        oppervlakte = float(input("Geef het aantal m2 dat gekuist moet worden: "))


if __name__ == '__main__':
    main()
