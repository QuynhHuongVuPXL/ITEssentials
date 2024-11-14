def bereken_lidgeld(leeftijd, aantal_kinderen, inkomen, aansluitingsjaar):
    JAAR_NU = 2023
    aanvangsgeld = 100
    vermindering_kind = 0

    if leeftijd > 60:
        aanvangsgeld -= 15

    if aantal_kinderen > 0:
        vermindering_kind += 7.5 * aantal_kinderen

    if vermindering_kind > 35:
        vermindering_kind = 35

    aanvangsgeld -= vermindering_kind


    if JAAR_NU - aansluitingsjaar > 20:
        aanvangsgeld -= 12.5

    if inkomen < 7500:
        aanvangsgeld -= 25

    if aanvangsgeld < 50:
        aanvangsgeld = 50

    return aanvangsgeld

def main():
    naam = str(input("Geef de naam in: "))
    while naam != "x" and naam != "X":
        leeftijd = int(input("Geef de leeftijd in: "))
        aantal_kinderen = int(input("Geef het aantal kinderen in: "))
        inkomen = int(input("Geef het inkomen in: "))
        aansluitingsjaar = int(input("Geef het aansluitingsjaar in: "))

        totaal_bedrag = bereken_lidgeld(leeftijd, aantal_kinderen, inkomen, aansluitingsjaar)
        print(f"voor {naam} bedraagt het lidgeld {totaal_bedrag}")

        naam = str(input("Geef de naam in: "))


if __name__ == '__main__':
    main()