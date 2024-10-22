def sorteer(tekst):
    resultaat = ""
    lengte = len(tekst)

    for i in range(lengte):
        kleinste_letter = tekst[0]
        for letter in tekst:
            if ord(letter) < ord(kleinste_letter):
                kleinste_letter = letter
        resultaat += kleinste_letter
        tekst = tekst.replace(kleinste_letter, "", 1)

    return resultaat


def main():
    tekst = "abdaba"

    resultaat = sorteer(tekst)
    print(resultaat)


if __name__ == '__main__':
    main()
