def omzetting(wisselkoers, bedrag):
    return wisselkoers * bedrag


def main():
    wisselkoers_input = float(input("Geef wisselkoers in: "))
    om_te_zetten_bedrag = float(input("Geef het om te zetten bedrag in euro in: "))

    while om_te_zetten_bedrag != 0:
        bedrag_in_dollar = omzetting(wisselkoers_input, om_te_zetten_bedrag)

        print("Het bedrag in dollar is", bedrag_in_dollar)

        om_te_zetten_bedrag = float(input("Geef het om te zetten bedrag in euro in: "))


if __name__ == '__main__':
    main()
