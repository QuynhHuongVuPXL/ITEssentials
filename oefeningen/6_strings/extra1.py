def main():
    tekst = str(input("Geef een tekst in: "))

    if len(tekst) % 3 == 0:
        tekst = tekst.upper()
    else:
        tekst = tekst.lower()

    print(tekst)

if __name__ == '__main__':
    main()