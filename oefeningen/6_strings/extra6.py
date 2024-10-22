def verander_klinker(zin, teken):
    resultaat = ""
    for karakter in zin:
        if karakter in "aeiouAEIOU":
            karakter = teken
        resultaat += karakter
    return resultaat


def main():
    zin = str(input("Geef zin in: "))
    teken = str(input("Geef teken in: "))

    resultaat = verander_klinker(zin, teken)
    print(resultaat)


if __name__ == '__main__':
    main()
