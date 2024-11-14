def bereken_prioriteitsnummer(gezin_sinkomen, aantal_kinderen, code):
    jaar_nu = 2023

    if code[0] == "J" and (jaar_nu - int(code[1:])) < 5:
        return 5
    elif gezin_sinkomen < 2000:
        if aantal_kinderen >= 3:
            return 1
        else:
            return 2
    elif gezin_sinkomen < 2500:
        return 3
    elif gezin_sinkomen >= 2500:
        return 4


def bepaling_bouwlening(naam_man, naam_vrouw, gezins_inkomen, aantal_kinderen):
    if (naam_man != "xx" and naam_vrouw == "xx") or (naam_man == "xx" and naam_vrouw != "xx"):
        if aantal_kinderen >= 1 and gezins_inkomen < 1500:
            return "J"
    return " "


def prioriteit_sterren(prioriteit):
    return "*" * prioriteit


def main():
    totaal = 0
    aantal_sociale_woning = 0
    hoogste_inkomen = 0
    status_hoogste_inkomen = ""

    string_output = "{:<2} {:<40} {:<10} {:<10} \n".format("nr", "familienaam", "prioriteit", "bouwlening")

    code = str(input("Geef code: "))

    while code != "S":
        naam_man = str(input("Geef naam (achternaam voornaam): "))
        naam_vrouw = str(input("Geef naam partner (achternaam voornaam): "))
        inkomen_man = int(input("Geef inkomen: "))
        inkomen_vrouw = int(input("Geef inkomen partner: "))
        gezins_inkomen = inkomen_man + inkomen_vrouw
        aantal_kinderen = int(input("Geef aantal kinderen: "))
        totaal += 1

        if gezins_inkomen > hoogste_inkomen:
            hoogste_inkomen = gezins_inkomen
            if naam_man != "xx" and naam_vrouw == "xx":
                status_hoogste_inkomen = "alleenstaande man"
            elif naam_man == "xx" and naam_vrouw != "xx":
                status_hoogste_inkomen = "alleenstaande vrouw"
            else:
                status_hoogste_inkomen = "gezin"

        if code[0] == "J":
            aantal_sociale_woning += 1

        split_naam_man = naam_man.split(" ")
        if len(split_naam_man) > 0:
            achternaam_man = split_naam_man[0]
        else:
            achternaam_man = ""

        if len(split_naam_man) > 1:
            voornaam_man = split_naam_man[1]
        else:
            voornaam_man = ""

        split_naam_vrouw = naam_vrouw.split(" ")
        if len(split_naam_vrouw) > 0:
            achternaam_vrouw = split_naam_vrouw[0]
        else:
            achternaam_vrouw = ""

        if len(split_naam_vrouw) > 1:
            voornaam_vrouw = split_naam_vrouw[1]
        else:
            voornaam_vrouw = ""

        if naam_man != "xx" and naam_vrouw == "xx":
            string_resultaat = f"Meneer {voornaam_man[0].upper()}. {achternaam_man}"
        elif naam_man == "xx" and naam_vrouw != "xx":
            string_resultaat = f"Mevrouw {voornaam_vrouw[0].upper()}. {achternaam_vrouw}"
        else:
            string_resultaat = f"De Heer en Mevrouw {voornaam_man[0].upper()}. {achternaam_man}-{achternaam_vrouw}"

        prioriteit = bereken_prioriteitsnummer(gezins_inkomen, aantal_kinderen, code)
        bouwlening = bepaling_bouwlening(naam_man, naam_vrouw, gezins_inkomen, aantal_kinderen)
        sterren = prioriteit_sterren(prioriteit)

        string_output += "{:<2} {:<40} {:<10} {:<10} \n".format(totaal, string_resultaat, sterren, bouwlening)

        code = str(input("Geef code: "))

    percentage_sociale_woning = aantal_sociale_woning / totaal * 100

    print(string_output)
    print("Percentage sociale woning: {}".format(percentage_sociale_woning))
    print(f"Hoogste inkomen: {float(hoogste_inkomen)} ({status_hoogste_inkomen})")


if __name__ == '__main__':
    main()

# duratie = "J1999"
# print(duratie[0])
# print(duratie[1:])
