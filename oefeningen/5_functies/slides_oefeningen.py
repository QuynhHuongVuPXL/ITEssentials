# # oef 5.1 met return
# def print_tekens(gekozen_teken, hoevaak_je_teken_wilt):
#     return str(gekozen_teken) * hoevaak_je_teken_wilt
#
#
# teken = "* "
# aantal = 8
# output = print_tekens(teken, aantal)
# print(output)

# # oef 5.1 met print
# def print_tekens(gekozen_teken, hoevaak_je_teken_wilt):
#     resultaat = gekozen_teken * hoevaak_je_teken_wilt
#     print(resultaat)
#
#
# def main():  # vanaf nu main gebruiken !!!!
#     teken = "* "
#     aantal = 8
#     print(print_tekens(teken, aantal))  # met een print in een print krijg je None, want je print een print
#     print()
#     print_tekens(teken, aantal)  # dit hoort geen None te geven, want je pakt alleen de print van de functie
#
#
# if __name__ == '__main__':
#     main()


# Wat gebeurt als we onderstaande programma's laten uitvoeren?

# The point of return is that it signals what the result is when calling the function.
# The point of print is that it puts some text on the screen.

# deze met een print geeft foutmelding, want print print iets maar geeft niks terug
# je kan pas iets met een functie doen als die functie ook een waarde heeft
# def print_bereken(a, b):
#     print(a ** 3 + b ** 2)
#
#
# x = 4 * print_bereken(1, 3)
# print(x)


# hier heeft die wel een waarde die gereturnd werd en hiermee kan je wel verder werken
# def bereken(a, b):
#     return a ** 3 + b ** 2
#
#
# x = 4 * bereken(1, 3)
# print(x)

# # oef 5.2
# def print_tekens(gekozen_teken, gekozen_breedte):
#     return gekozen_teken * gekozen_breedte
#
#
# def print_rechthoek(hoogte, teken, breedte):
#     resultaat = ""
#     for i in range(hoogte):
#         resultaat += print_tekens(teken, breedte)
#         resultaat += "\n"
#     print(resultaat)
#
#
# def main():
#     hoogte = int(input("Geef een hoogte in: "))
#     breedte = int(input("Geef een breedte in: "))
#     teken = "* "
#
#     print_rechthoek(hoogte, teken, breedte)
#
#
#
# if __name__ == "__main__":
#     main()

# # oef 5.3
# def printx():
#     print("x")  # als return doorgeven naar volgende functie
#     # als ik hier print gebruik dan in de volgende functie hoef ik geen print, want anders krijg ik None
#
#
# def meerderex(aantal):
#     for i in range(aantal):
#         printx()  # hier hoef ik dan niet nog een keer return naar main te doen, maar kan ik printen
#
#         # anders kan je hier ook een return doen en dan in main opvangen in een variabele
#
#
# def main():
#     aantal = int(input("Geef aan hoevaak je x wilt printen: "))
#
#     meerderex(aantal)

#
# if __name__ == '__main__':
#     main()

# # oef 5.4 en 5.5
#
# def is_even(gekozen_getal):
#     return gekozen_getal % 2 == 0
#
#
# def is_oneven(getal):
#     return not is_even(getal)
#
#
# def main():
#     getal = int(input("Geef een getal in: "))
#     output = is_even(getal)  # oneven geeft true als oneven is, daarom is_even gebruiken
#     print("Is het getal even?", output)
#
#
# if __name__ == '__main__':
#     main()

# # oef 5.6
# def get_tienden(getal):
#     print(int(getal * 10 % 10))  # als je hier print kan je  in main gewoon oproepen
#     # als je hier return moet je een var maken in main en deze oproepen en dan printen
#
#
# def main():
#     getal = float(input("Geef een getal: "))
#
#     get_tienden(getal)
#
#
# if __name__ == '__main__':
#     main()

# # oef 5.7
# def toon_tafel(tafel):  # parameter
#     for i in range(0, 10 + 1):
#         output = i * tafel
#         print(f"{i} x {tafel} = {output}")
#
#
# def main():
#     tafel = int(input("Geef een tafel: "))  # lokale variabele
#
#     toon_tafel(tafel)
#
#
# if __name__ == '__main__':
#     main()

# oef 5.8

# def verschuldigde_belasting(bedrag):
#     resultaat = 0
#     if bedrag <= 25000:
#         resultaat += bedrag * 0.384
#     elif bedrag <= 55000:
#         resultaat += bedrag * 0.384
#         resultaat += (bedrag - 25000) * 0.50
#     else:
#         resultaat += bedrag * 0.384
#         resultaat += (bedrag - 25000) * 0.50
#         resultaat += (bedrag - 55000) * 0.60
#
#     return resultaat
#
# def main():
#     bedrag = float(input("Geef een belastbaar bedrag in: "))
#
#     belasting = verschuldigde_belasting(bedrag)
#
#     print("De verschuldigde belasting is:", belasting, "euro")
#
# if __name__ == '__main__':
#     main()


# # random module
# import random
#
#
# def main():
#     random.seed(1)  # met seed geeft het dezelfde random getallen
#     print(random.randint(4, 10))
#     random.seed(1)  # dan krijg je opnieuw dezelfde getallen, met seed kan je afdwingen dat je dezelfde getallen krijgt
#     print(random.randint(4, 10))
#
#     print(random.random())  # dit geeft een random getal tussen 0 en 1
#
#
# if __name__ == '__main__':
#     main()

# oef 5.9

import random


def main():
    # # 1 een willekeurig geheel getal genereert ≥ 0 en ≤ 10
    # willekeurig_geheel_getal = random.randint(0, 10)
    # print(willekeurig_geheel_getal)

    # # 2 10 willekeurige gehele getallen genereert > 0 en < 10
    # for i in range(10):
    #     willekeurig_geheel_getal = random.randint(0, 10)
    #     print(willekeurig_geheel_getal)

    # # 3 een willekeurig geheel getal genereert ≥ -200 en ≤ 1000 dat een veelvoud is van 10
    # random_number = random.randint(-200, 1000)
    #
    # while random_number % 10 != 0:
    #     random_number = random.randint(-200, 1000)
    #
    # print(random_number)

    # 4 een willekeurig reëel getal genereert ≥ 0 en <100 met juist 1 cijfer na de komma
    random_int_getal = random.randint(0, 99)
    random_float_getal = random.random()

    resultaat = random_int_getal + random_float_getal

    print(round(resultaat, 1))

    # print(type(resultaat))


if __name__ == '__main__':
    main()
