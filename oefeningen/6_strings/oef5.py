def bereken_prijs_per_volwassenen(hotelcode, aantal_sterren):
    if hotelcode[:2] == "HI":
        prijs_volwassenen = 70
    else:
        if aantal_sterren <= 2:
            prijs_volwassenen = 48
        elif aantal_sterren == 3:
            if hotelcode[:2] == "BR" or hotelcode[:2] == "AN":
                prijs_volwassenen = 60
            else:
                prijs_volwassenen = 56
        else:
            prijs_volwassenen = 60

    return prijs_volwassenen


def bereken_prijs_kind(kindercode, aantal_sterren, hotelcode):
    prijs_volwassenen = bereken_prijs_per_volwassenen(hotelcode, aantal_sterren)
    if kindercode == "A":
        if aantal_sterren <= 2 and not hotelcode[:2] == "BR":
            prijs_kind = 0
        else:
            prijs_kind = prijs_volwassenen * 0.50
    else:
        prijs_kind = prijs_volwassenen * 0.50

    return prijs_kind


def print_sterren(aantal_sterren):
    return aantal_sterren * "*"


def main():
    output = ""

    aantal_volwassenen = int(input("Geef het aantal volwassenen: "))
    aantal_kinderen = int(input("Geef het aantal kinderen: "))
    hotelcode = str(input("Geef een hotelcode: "))

    while hotelcode != "/":
        aantal_sterren = int(input("Geef het aantal sterren: "))
        kindercode = str(input("Geef een kindercode: "))

        while not (len(kindercode) == 1 and ord(kindercode) >= 65 and ord(kindercode) <= 90):
            kindercode = str(input("Geef een geldige kindercode: "))

        prijs_volwassen = bereken_prijs_per_volwassenen(hotelcode, aantal_sterren)
        prijs_kind = bereken_prijs_kind(kindercode, aantal_sterren, hotelcode)
        totaal_prijs = (prijs_volwassen * aantal_volwassenen) + (prijs_kind * aantal_kinderen)
        sterren = print_sterren(aantal_sterren)

        output += "{}{:<5} {:<5.2f} {:<5.2f} {:<5.2f}\n".format(hotelcode, sterren, prijs_volwassen, prijs_kind, totaal_prijs)

        hotelcode = str(input("Geef een hotelcode: "))

    print(output)


if __name__ == '__main__':
    main()
