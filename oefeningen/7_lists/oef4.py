def main():
    letterlijst = []
    voorkomens = [0] * 26  # frequentie tabel maken
    output = ""
    gecontroleerde_letters = []

    tekst = "abc Abc 123 z".lower()

    # for letter in tekst:
    #     if letter >= 'a' and letter <= 'z':
    #         index = ord(letter) - ord('a')
    #         voorkomens[index] += 1
    #         letterlijst.append(letter)
    #
    # for letter in letterlijst:
    #     print(f"{letter} aantal voorkomens:\n")
    #
    # print(letterlijst)
    # print(voorkomens)

    for letter in tekst:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letterlijst.append(letter)

    for letter in letterlijst:
        if letter not in gecontroleerde_letters:
            aantal_voorkomens = 0
            for i in letterlijst:
                if i == letter:
                    aantal_voorkomens += 1

            output += f"{letter} aantal voorkomens: {aantal_voorkomens} \n"
            gecontroleerde_letters.append(letter)

    print(output)


if __name__ == '__main__':
    main()

