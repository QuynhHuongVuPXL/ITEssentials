def main():
    alfabet = ""
    for i in range(97, 123):
        if (i - 97) % 2 != 0:
            alfabet += chr(i).upper()
        else:
            alfabet += chr(i)

    alfabet = alfabet.replace("H", "X")

    print(alfabet)


if __name__ == '__main__':
    main()
