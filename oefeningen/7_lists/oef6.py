def bepaal_sterrenbeeld(dag, maand):
    sterrenbeelden = ["waterman", "vissen", "ram", "stier", "tweelingen", "kreeft", "leeuw", "maagd",
                      "weegschaal", "schorpioen", "boogschutter", "steenbok"]

    index = maand - 1

    if dag < 21:
        index = index - 1

    return sterrenbeelden[index]


def print_naam(voornaam, achternaam):
    return f"{voornaam[0].upper()}. {achternaam.upper()}"


def main():
    naam = str(input("Geef de naam van een persoon in / om te eindigen: "))

    while naam != "/":
        voornaam = str(input("Geef de voornaam: "))
        geboortedatum = str(input("Geef geboortedatum: "))

        dag = int(geboortedatum.split("/")[0])
        maand = int(geboortedatum.split("/")[1])

        sterrenbeeld = bepaal_sterrenbeeld(dag, maand)
        output_naam = print_naam(voornaam, naam)

        print(output_naam, sterrenbeeld)

        naam = str(input("Geef de naam van een persoon in / om te eindigen: "))


if __name__ == '__main__':
    main()
