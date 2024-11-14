def bereken_boete(aantal_boeken, aantal_dagen_te_laat):
    boete = 0.07 * aantal_boeken * aantal_dagen_te_laat

    if aantal_dagen_te_laat >= 45:
        boete += 0.84

    return boete

def main():
    aantal_aanmaningsbrieven = 0
    naam = str(input("Geef de naam in: "))
    while naam != "xx":
        aantal_boeken = int(input("Geef het aantal boeken in: "))
        aantal_dagen_te_laat = int(input("Geef het aantal dagen te laat in: "))

        if aantal_dagen_te_laat >= 45:
            aantal_aanmaningsbrieven += 1

        boete = bereken_boete(aantal_boeken, aantal_dagen_te_laat)
        print(f"{naam} heeft een boete van {boete}")

        naam = str(input("Geef de naam"))

    print("aantal aanmaningsbrieven " + str(aantal_aanmaningsbrieven) + "")

if __name__ == '__main__':
    main()