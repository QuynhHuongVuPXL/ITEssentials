def bereken_hoogte():
    hoogte = float(input("Geef de hoogte van de poort: "))
    while not 2 <= hoogte <= 6.5:
        hoogte = float(input("Geef de hoogte van de poort: "))

    return hoogte


def bereken_breedte():
    breedte = float(input("Geef de breedte van de poort: "))
    while not 2 <= breedte <= 8:
        breedte = float(input("Geef de breedte van de poort: "))

    return breedte


def bereken_oppervlakte(hoogte, breedte):
    return hoogte * breedte


def bereken_gewicht(oppervlakte):
    return oppervlakte * 11


def geef_prijs_motornaam(gewicht):
    if gewicht > 300:
        return "X300", 250.5
    elif 150 <= gewicht <= 300:
        return "A105", 220.5
    else:
        return "A101", 120


def bereken_totaalprijs(oppervlakte, motor_prijs, speciale_kleur):
    basisprijs = oppervlakte * 113.5
    if speciale_kleur == "j":
        basisprijs *= 1.10
    return basisprijs + motor_prijs

def genereer_offertenummer(naam, totaal_prijs):
    totaal_prijs_integer = int(totaal_prijs)
    omgekeerde_prijs = str(totaal_prijs_integer)[::-1]
    naam_upper = naam.upper()
    return f"2023_{naam_upper}_{omgekeerde_prijs}"



def main():
    naam = str(input("Geef de naam van de verkoper: "))
    hoogte = bereken_hoogte()
    breedte = bereken_breedte()
    speciale_kleur = str(input("Wilt u een speciale kleur? (j/n): "))

    oppervlakte = bereken_oppervlakte(hoogte, breedte)
    gewicht = bereken_gewicht(oppervlakte)
    motornaam, motor_prijs = geef_prijs_motornaam(gewicht)
    totaalprijs = bereken_totaalprijs(oppervlakte, motor_prijs, speciale_kleur)
    offertenummer = genereer_offertenummer(naam, totaalprijs)

    print(offertenummer)

if __name__ == '__main__':
    main()
