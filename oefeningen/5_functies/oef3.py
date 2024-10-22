def bereken_lidgeld(aanvangsgeld, leeftijd, aantal_kinderen, inkomen, aansluitingsjaar):
    jaar_nu = 2023
    aanvangsgeld = 100
    vermindering_kind_geld = 0

    if leeftijd > 60:
        aanvangsgeld -= 15

    if aantal_kinderen > 0:
        vermindering_kind_geld += aantal_kinderen * 7.5

    if vermindering_kind_geld > 35:
        vermindering_kind_geld = 35

    aanvangsgeld -= vermindering_kind_geld

    # aanvangsgeld -= min(35, 7.5 * kinderen)

    if jaar_nu - aansluitingsjaar > 20:
        aanvangsgeld -= 12.5

    if inkomen < 7500:
        aanvangsgeld -= 25

    if aanvangsgeld < 50:
        aanvangsgeld = 50

    # aanvangsgeld = max(50,aanvangsgeld)

    return aanvangsgeld


def main():
    aanvangsgeld = 100

    naam = str(input("Geef de naam in: "))

    while naam != "X" and naam != "x":
        leeftijd = int(input("Geef de leeftijd in: "))
        aantal_kinderen = int(input("Geef het aantal kinderen in: "))
        inkomen = int(input("Geef het inkomen in: "))
        aansluitingsjaar = int(input("Geef het aansluitingsjaar in: "))

        lidgeld = bereken_lidgeld(aanvangsgeld, leeftijd, aantal_kinderen, inkomen, aansluitingsjaar)

        print("voor", naam, "bedraagt het lidgeld", lidgeld)

        naam = str(input("Geef de naam in: "))


if __name__ == '__main__':
    main()
