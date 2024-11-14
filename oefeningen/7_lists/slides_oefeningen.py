# # oef 1
# fruitlist = ["appel", "banaan", "kers", "mango"]
# print("Aantal elementen in fruitlist:", len(fruitlist))
# teller = 0
# while teller < len(fruitlist):
#     print(fruitlist[teller])
#     teller += 1

# # oef 2
# numberlist = [314, 315, 1001, 642, 246, 129, 999]
# grootste_nummer = numberlist[0]
# kleinste_nummer = numberlist[0]
# som = 0
# for number in numberlist:
#     som += number
#
#     if number > grootste_nummer:
#         grootste_nummer = number
#
#     if number < kleinste_nummer:
#         kleinste_nummer = number
#
# print("Grootste nummer:", grootste_nummer)
# print("Kleinste nummer:", kleinste_nummer)
# print("De som van alle nummers:", som)  # als je concatination gebruikt dan moet je omzetten naar een string (+)

# # oef 3
# def main():
#     getallen_lijst = []
#     getal = int(input("Geef een getal: "))
#     while getal != 0:
#         if getal in getallen_lijst:
#             print("Dit getal staat al op index", getallen_lijst.index(getal))
#             getallen_lijst.remove(getal)
#             getallen_lijst.append(getal)
#         else:
#             getallen_lijst.append(getal)
#
#         getal = int(input("Geef een getal: "))
#
#     print(getallen_lijst)
#
#
# if __name__ == '__main__':
#     main()

# # oef 4
# def main():
#     getallen_lijst = []
#     aantal_getallen = 10
#     getal_kleiner_dan_gemiddelde = 0
#     totaal = 0
#     for i in range(aantal_getallen):
#         getal = int(input(f"Geef getal {i + 1} in: "))
#         getallen_lijst.append(getal)
#
#     for i in getallen_lijst:
#         totaal += i
#
#     gemiddelde = totaal / aantal_getallen
#
#     for i in getallen_lijst:
#         if i < gemiddelde:
#             getal_kleiner_dan_gemiddelde += 1
#
#     # print(getallen_lijst)
#     # print(totaal)
#     print("Het gemiddelde is:" + str(gemiddelde))
#     print("Aantal getallen kleiner dan het gemiddelde" + str(getal_kleiner_dan_gemiddelde))
#
#
# if __name__ == '__main__':
#     main()

# # oef 5
# def bepaal_voorkomen(lijst, element):
#     aantal = 0
#     indexen = []
#     index = 0
#     for i in lijst:
#         if i == element:
#             aantal += 1
#             indexen.append(index)
#         index += 1
#
#     print(f"Het element {element} komt {aantal} keer voor")
#     print(f"Indexen van {element}: {indexen}")
#
#
# def main():
#     fruitlist = ["appel", "banaan", "kers", "mango", "banaan", "kers", "mango", "mango", "mango"]
#     element = "mango"
#
#     bepaal_voorkomen(fruitlist, element)
#
#
# if __name__ == '__main__':
#     main()

# # oef 6
# def cumulative_sum(lijst):
#     som = 0
#     cumulatieve_lijst = []
#     for i in lijst:
#         som += i
#         cumulatieve_lijst.append(som)
#
#     print(cumulatieve_lijst)
#
#
# def main():
#     numberlist = [5, 10, 15, 20, 25, 30, 35]
#     fruitlist = ["appel", "banaan", "kers", "mango", "banaan", "kers", "mango", "mango", "mango"]
#     print(numberlist)
#     cumulative_sum(numberlist)
#
#
# if __name__ == '__main__':
#     main()

# oef 7
def get_number_of_participants(lijst):
    return len(lijst[0])  # aantal kolommen


def get_number_of_tests(lijst):
    return len(lijst)  # aantal rijen als je geen [0] in geeft


def highest_heart_rate(lijst):
    hoogste_hartslag = lijst[0][0]
    for test in lijst:
        for hartslag in test:
            if hartslag > hoogste_hartslag:
                hoogste_hartslag = hartslag

    return hoogste_hartslag


def lowest_heart_rate(lijst):
    laagste_hartslag = lijst[0][0]
    for test in lijst:
        for hartslag in test:
            if hartslag < laagste_hartslag:
                laagste_hartslag = hartslag

    return laagste_hartslag


def average_heart_rate(lijst):
    aantal_deelnemers = get_number_of_tests(lijst)
    gemiddelden = []

    for test in lijst:
        totaal_hartslag = 0
        for hartslag in test:
            totaal_hartslag += hartslag
        gemiddelde = totaal_hartslag / len(test)
        gemiddelden.append(round(gemiddelde, 1))

    return gemiddelden


def heart_rate_difference(lijst):
    aantal_deelnemers = len(lijst[0])
    verschillen = []

    for i in range(aantal_deelnemers):
        hoogste_hartslag = lijst[0][i]
        laagste_hartslag = lijst[0][i]

        for test in lijst:
            hartslag = test[i]
            if hartslag > hoogste_hartslag:
                hoogste_hartslag = hartslag
            if hartslag < laagste_hartslag:
                laagste_hartslag = hartslag

        verschil = hoogste_hartslag - laagste_hartslag
        verschillen.append(verschil)

    return verschillen


def main():
    testresultaten = [
        [72, 75, 71, 73, 72, 76],
        [91, 90, 94, 93, 88, 91],
        [130, 135, 139, 142, 129, 138],
        [120, 118, 110, 105, 121, 119]
    ]

    aantal_deelnemers = get_number_of_participants(testresultaten)
    aantal_testen = get_number_of_tests(testresultaten)
    hoogste_hartslag = highest_heart_rate(testresultaten)
    laagste_hartslag = lowest_heart_rate(testresultaten)
    gemiddelde = average_heart_rate(testresultaten)
    verschillen = heart_rate_difference(testresultaten)

    print("Het aantal deelnemers zijn " + str(aantal_deelnemers))
    print("Het aantal testen zijn " + str(aantal_testen))
    print("Het hoogste hartslag is " + str(hoogste_hartslag))
    print("Het laagste hartslag is " + str(laagste_hartslag))
    print("Het gemiddelde hartslag voor elke test is " + str(gemiddelde))
    print("De verschillen in hartslag voor elke deelnemer is " + str(verschillen))


if __name__ == '__main__':
    main()
