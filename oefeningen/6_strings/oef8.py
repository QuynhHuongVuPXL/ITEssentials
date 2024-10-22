def main():
    start_karakter = str(input("Geef het start-karakter: "))
    aantal_rijen = int(input("Geef het aantal rijen: "))

    ascii_code = ord(start_karakter)

    for i in range(1, aantal_rijen + 1):
        for j in range(i):
            print(chr(ascii_code), end=" ")
            ascii_code += 1

            if ascii_code > ord("Z"):
                ascii_code = ord("A")

        print()


if __name__ == '__main__':
    main()
