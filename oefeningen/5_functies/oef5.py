def controleer(lidnummer):
    tweede_getal = lidnummer // 100000 % 10
    vierde_getal = lidnummer // 1000 % 10
    voorlaatste_getal = lidnummer // 10 % 10
    laatste_getal = lidnummer % 10

    if (voorlaatste_getal == tweede_getal) and (laatste_getal == vierde_getal):
        print("gratis")
    else:
        print("niet gratis")


def main():
    nummer = int(input("Geef een nummer bestaande uit 7 cijfers in: "))

    controleer(nummer)


if __name__ == '__main__':
    main()

# voorbeeld = 1734568
#
# voorlaatste_getal = voorbeeld // 10 % 10
# print(voorlaatste_getal)
#
# laatste_getal = voorbeeld % 10
# print(laatste_getal)
#
# tweede_getal = voorbeeld // 100000 % 10
# print(tweede_getal)
#
# vierde_getal = voorbeeld // 1000 % 10
# print(vierde_getal)
