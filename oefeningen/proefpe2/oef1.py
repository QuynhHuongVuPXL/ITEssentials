def druk_tekst(tekst):
    output = ""

    for letter in tekst[::-1]:
        output += letter
        print(output)


def main():
    tekst = input("geef een tekst in: ")

    druk_tekst(tekst)


if __name__ == '__main__':
    main()

