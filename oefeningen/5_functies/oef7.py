def bereken_boete(aantal_boeken, aantal_dagen):
    boete = 0.07 * aantal_boeken * aantal_dagen

    if aantal_dagen > 44:
        boete += 0.84

    return boete


def main():
    aanmanings_brieven = 0

    naam = str(input("Geef de naam in: "))

    while naam != "xx":
        aantal_boeken = int(input("Geef het aantal boeken in: "))
        aantal_dagen_te_laat = int(input("Geef het aantal dagen te laat in: "))

        if aantal_dagen_te_laat > 44:
            aanmanings_brieven += 1

        boete = bereken_boete(aantal_boeken, aantal_dagen_te_laat)
        print(f"{naam} heeft een boete van {boete} euro")

        naam = str(input("Geef de naam in: "))

    print("Het aantal aanmaningsbrieven:", aanmanings_brieven)


if __name__ == '__main__':
    main()
