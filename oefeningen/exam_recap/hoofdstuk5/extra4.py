def bereken_kosten_wagen(type_wagen, afstand_in_km):
    vaste_som = 0
    if type_wagen == "R":
        if afstand_in_km < 10:
            vaste_som += 25
        elif afstand_in_km <= 20:
            vaste_som += 25
            vaste_som += (afstand_in_km - 10) * 2.25
        else:
            vaste_som += 25
            vaste_som += 10 * 2.25
            vaste_som += (afstand_in_km - 20) * 1.75
    else:
        if afstand_in_km <= 10:
            vaste_som += 20
        elif afstand_in_km <= 20:
            vaste_som += 20
            vaste_som += (afstand_in_km - 10) * 1.75
        else:
            vaste_som += 20
            vaste_som += 10 * 1.75
            vaste_som += (afstand_in_km - 20) * 1.15

    kosten_wagen = vaste_som
    return kosten_wagen


def bereken_kosting_mutualiteit(type_wagen, afstand_in_km, lid_mutualiteit):
    vaste_som = 0
    if lid_mutualiteit == "J":
        if type_wagen == "R":
            vaste_som += 15
            if afstand_in_km > 10:
                vaste_som += (afstand_in_km - 10) * 1.15
        else:
            vaste_som += 10
            if afstand_in_km > 10:
                vaste_som += (afstand_in_km - 10) * 1

    korting_mutualiteit = vaste_som
    return korting_mutualiteit


def main():
    totaal_slachtoffers = 0
    aantal_lid_mutualiteit = 0

    naam = str(input("Geef een naam in: "))

    while naam != "/":
        type_wagen = str(input("Geef reanimatie- of ziekenwagen (R/Z): "))
        afstand_in_km = float(input("Geef de afstand in km: "))
        lid_mutualiteit = str(input("Lid mutualiteit (J/N): "))
        totaal_slachtoffers += 1

        if lid_mutualiteit == "J":
            aantal_lid_mutualiteit += 1

        kosten_wagen = bereken_kosten_wagen(type_wagen, afstand_in_km)
        korting_mutualiteit = bereken_kosting_mutualiteit(type_wagen, afstand_in_km, lid_mutualiteit)

        totale_kostprijs = kosten_wagen - korting_mutualiteit

        print(f"{naam}: totale kostprijs {kosten_wagen}, netto kostprijs {totale_kostprijs}")
        print()


        naam = str(input("Geef een naam in: "))

    print(f"Het aantal vervoerde slachtoffers: {totaal_slachtoffers}")
    percentage_lid_mutualiteit = aantal_lid_mutualiteit / totaal_slachtoffers * 100
    print(f"Het percentage dat lid is van de mutualiteit: {round(percentage_lid_mutualiteit, 2)}")


if __name__ == '__main__':
    main()
