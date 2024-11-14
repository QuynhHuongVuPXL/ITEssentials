def main():
    lijst = ["nul", "een", "twee", "drie", "vier", "vijf", "zes", "zeven", "acht", "negen"]
    output = ""

    geheel_getal = str(input("Geef een geheel getal: "))

    for getal in geheel_getal:
        output += lijst[int(getal)] + " "

    print(output)


if __name__ == '__main__':
    main()
