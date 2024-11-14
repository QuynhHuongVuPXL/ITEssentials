# def bepaal_leeftijd(huidige_datum, deelnemer_geboortedatum):
#     dag_nu = int(huidige_datum.split("/")[0])
#     maand_nu = int(huidige_datum.split("/")[1])
#     jaar_nu = int(huidige_datum.split("/")[2])
#
#     geboorte_dag = int(deelnemer_geboortedatum.split('/')[0])
#     geboorte_maand = int(deelnemer_geboortedatum.split('/')[1])
#     geboorte_jaar = int(deelnemer_geboortedatum.split('/')[2])
#
#     leeftijd = jaar_nu - geboorte_jaar
#
#     if maand_nu < geboorte_maand or (maand_nu == geboorte_maand and dag_nu < geboorte_dag):
#         leeftijd -= 1
#
#     return leeftijd
#
# def bepaal_resultaat(lijst_correcte_antwoorden, lijst_deelnemer_antwoorden):
#     punten = 0
#     for correcte_antwoord in lijst_correcte_antwoorden:
#         for deelnemer_antwoord in lijst_deelnemer_antwoorden:
#             if correcte_antwoord == deelnemer_antwoord:
#                 punten += 2
#             else:
#                 punten -= 1
#         punten += 0
#
#     return punten
#
#
#
#
# def main():
#     output = ""
#     lijst_correcte_antwoorden = []
#     lijst_deelnemer_antwoorden = []
#
#     correcte_antwoorden = str(input("Geef de correcte antwoorden op de vragen: "))
#     lijst_correcte_antwoorden.append(correcte_antwoorden)
#     huidige_datum = str(input("Geef de huidige datum (dd/mm/yyy): "))
#     deelnemer_informatie = str(input("Geef deelnemer informatie: "))
#
#     while deelnemer_informatie != 0:
#         deelnemer_nummer = deelnemer_informatie.split(" ")[0]
#         deelnemer_geboortedatum = deelnemer_informatie.split(" ")[1]
#         deelnemer_antwoorden = deelnemer_informatie.split(" ")[2]
#         lijst_deelnemer_antwoorden.append(deelnemer_antwoorden)
#         deelnemer_tijd = deelnemer_informatie.split(" ")[3]
#
#
#
#         leeftijd = bepaal_leeftijd(huidige_datum, deelnemer_geboortedatum)
#
#
#         deelnemer_informatie = str(input("Geef deelnemer informatie: "))
#
#
# if __name__ == '__main__':
#     main()
#
#


lijst_correcte_antwoorden = []
lijst_deelnemer_antwoorden = []

correcte_antwoorden = "AAAAAAAAAA"
for letter in correcte_antwoorden:
    lijst_correcte_antwoorden.append(letter)

deelnemer_antwoorden = "AAAAABBEEE"
for letter in deelnemer_antwoorden:
    lijst_deelnemer_antwoorden.append(letter)

punten = 20

for correcte_antwoord in lijst_correcte_antwoorden:
    print(correcte_antwoord)
    for deelnemer_antwoord in lijst_deelnemer_antwoorden:
        print(deelnemer_antwoorden)
        if correcte_antwoord == deelnemer_antwoord:
            punten += 2


print(punten)
