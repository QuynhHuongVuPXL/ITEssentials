def keer_om_n(tekst, n):
    resultaat = ""
    for letter in tekst:
        resultaat += letter * n

    return resultaat[::-1]


def main():
    print(keer_om_n("tien", 5))


if __name__ == '__main__':
    main()
