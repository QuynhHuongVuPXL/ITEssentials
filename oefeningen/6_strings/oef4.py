def eerste_helft(tekst1):
    if len(tekst1) < 4:
        return tekst1.upper() + (4 - len(tekst1)) * "*"
    else:
        return tekst1.upper()

def tweede_helft(tekst2):
    if len(tekst2) < 4:
        return (4 - len(tekst2)) * "+" + tekst2.lower()
    else:
        return tekst2.lower()


def main():
    tekst1 = "a"
    tekst2 = "GH"

    print(eerste_helft(tekst1) + tweede_helft(tekst2))


if __name__ == '__main__':
    main()
