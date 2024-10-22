def vercijfer(tekst):
    resultaat = ""

    for karakter in range(0, len(tekst), 5):
        groep = tekst[karakter:karakter + 5]

        if len(groep) == 5:
            resultaat += groep[::-1]
        else:
            resultaat += groep

    return resultaat


def main():
    tekst = "toegepasteinformatica"
    vercijferde_tekst = vercijfer(tekst)

    print(vercijferde_tekst)


if __name__ == '__main__':
    main()
