def bepaal_gratis(lidnummer):
    tweede_nummer = lidnummer // 100000 % 10
    vierde_nummer = lidnummer // 1000 % 10
    zesde_nummer = lidnummer // 10 % 10
    zevende_nummer = lidnummer // 1 % 10

    if tweede_nummer == zesde_nummer and vierde_nummer == zevende_nummer:
        return "gratis"
    else:
        return "niet gratis"


def main():
    lidnummer = int(input("Geef een nummer bestaande uit 7 cijfers "))

    bepaling = bepaal_gratis(lidnummer)
    print(bepaling)


if __name__ == '__main__':
    main()

# nummer = 1734568
# print(nummer // 100000 % 10)
# print(nummer // 1000 % 10)
# print(nummer // 10 % 10)
# print(nummer // 1 % 10)
