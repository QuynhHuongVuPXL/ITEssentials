def vervorm(tekst):
    groep1 = ""
    groep2 = ""
    groep3 = ""

    for i in range(len(tekst)):
        if i % 3 == 0:
            groep1 += tekst[i]
        elif i % 3 == 1:
            groep2 += tekst[i]
        else:
            groep3 += tekst[i]

    return groep1 + groep2 + groep3


def main():
    tekst = "toegepasteinformatica"
    resultaat = vervorm(tekst)
    print(resultaat)


if __name__ == '__main__':
    main()
