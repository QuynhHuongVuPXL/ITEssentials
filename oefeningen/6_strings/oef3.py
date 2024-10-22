def main():
    aantal_karakters = int(input("Hoeveel karakters wil u ingeven? "))

    som = 0

    for karakters in range(aantal_karakters):
        een_karakter = input("Geef een karakter: ")

        if ord(een_karakter) >= 65 and ord(een_karakter) <= 90:
            resultaat = f"{een_karakter} is een hoofdletter"
        elif ord(een_karakter) >= 97 and ord(een_karakter) <= 122:
            resultaat = f"{een_karakter} is een kleine letter"
        elif ord(een_karakter) >= 48 and ord(een_karakter) <= 57:
            som += int(een_karakter)
            resultaat = f"Som cijfers: {som}"
        else:
            resultaat = f"{een_karakter} is onbekend"

        print(resultaat)


if __name__ == '__main__':
    main()

#         if ord(letter) < 97 or ord(letter) > 122:
