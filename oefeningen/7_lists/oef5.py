def print_kandidaten(kandidaten_lijst):
    nummer = 1
    for kandidaat in kandidaten_lijst:
        print(f"{nummer}: {kandidaat}")
        nummer += 1


def main():
    kandidaten_lijst = ["An Janssen", "Bart Vriends", "Andries Michels", "Inge Kaas"]

    totaal = 0
    keuze_janssen = 0
    keuze_vriends = 0
    keuze_michels = 0
    keuze_kaas = 0

    print_kandidaten(kandidaten_lijst)
    keuze = int(input("Maak uw keuze: "))

    while keuze != 0:
        totaal += 1
        print_kandidaten(kandidaten_lijst)

        if keuze == 1:
            keuze_janssen += 1
        elif keuze == 2:
            keuze_vriends += 1
        elif keuze == 3:
            keuze_michels += 1
        elif keuze == 4:
            keuze_kaas += 1

        keuze = int(input("Maak uw keuze: "))

    if totaal > 0:
        gemiddelde_janssen = keuze_janssen / totaal * 100
        gemiddelde_vriends = keuze_vriends / totaal * 100
        gemiddelde_michels = keuze_michels / totaal * 100
        gemiddelde_kaas = keuze_kaas / totaal * 100

        print(f"An Janssen : {keuze_janssen} = {gemiddelde_janssen:.1f}%")
        print(f"Bart Vriends : {keuze_vriends} = {gemiddelde_vriends:.1f}%")
        print(f"Andries Michels : {keuze_michels} = {gemiddelde_michels:.1f}%")
        print(f"Inge Kaas : {keuze_kaas} = {gemiddelde_kaas:.1f}%")


if __name__ == '__main__':
    main()
