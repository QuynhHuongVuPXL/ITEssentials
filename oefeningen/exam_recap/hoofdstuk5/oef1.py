def omzetting_van_bedrag(wisselkoers, bedrag):
    return wisselkoers * bedrag


def main():
    wisselkoers = float(input("Geef wisselkoers in: "))
    om_te_zetten_bedrag = float(input("Geef het om te zetten bedrag in:"))

    while om_te_zetten_bedrag != 0:
        bedrag_in_dollar = omzetting_van_bedrag(wisselkoers, om_te_zetten_bedrag)
        print("Bedrag in dollar is " + str(bedrag_in_dollar))

        om_te_zetten_bedrag = float(input("Geef het om te zetten bedrag in:"))


if __name__ == '__main__':
    main()
