import random


def main():
    aantal_groter_dan_5000 = 0
    getallenlijst = []
    for i in range(500):
        random_getal = random.randint(0, 10000)
        getallenlijst.append(random_getal)

    for getal in getallenlijst:
        if getal > 5000:
            aantal_groter_dan_5000 += 1

    som_groter_dan_5000 = 0

    if aantal_groter_dan_5000 >= 250:
        ondergrens = 8000
    else:
        ondergrens = 5000

    for getal in getallenlijst:
        if getal > ondergrens:
            som_groter_dan_5000 += getal

    #
    # if aantal_groter_dan_5000 < 250:
    #     som_groter_dan_5000 = 0
    #     for getal in getallenlijst:
    #         if getal > 5000:
    #             som_groter_dan_5000 += getal
    #     print(f"Som van getallen groter dan 5000: {som_groter_dan_5000}")
    # else:
    #     som_groter_dan_8000 = 0
    #     for getal in getallenlijst:
    #         if getal > 8000:
    #             som_groter_dan_8000 += getal
    #     print(f"Som van getallen groter dan 8000: {som_groter_dan_8000}")


if __name__ == '__main__':
    main()
