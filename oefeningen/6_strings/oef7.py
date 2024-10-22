import random


def encrypteer_tekst(tekst, getal):
    geencrypteerde_tekst = ""
    for karakter in tekst:
        geencrypteerded_karakter = chr(ord(karakter) + getal)
        geencrypteerde_tekst += geencrypteerded_karakter

    return geencrypteerde_tekst


def main():
    getal = 8
    # getal = random.randint(2, 24)
    #
    # while getal % 2 != 0:
    #     getal = random.randint(2, 24)

    print(f"(met random getal {getal})")

    tekst = str(input("Geef een tekst: "))

    resultaat = encrypteer_tekst(tekst, getal)

    print(resultaat)


if __name__ == '__main__':
    main()
