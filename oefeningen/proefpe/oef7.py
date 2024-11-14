def main():
    # som = 0  # initialize dit
    aantal_reeksen = int(input("Hoeveel reeksen wil je ingeven? "))  # gebruik int om te casten naar int
    for reeks in range(aantal_reeksen):  # als die gecast is naar int kan je range doen
        som = 0  # initialize dit in de loop zodat elke keer opnieuw 0 totaal in reeks

        getal = int(input("Geef een getal (0 om te eindigen): "))  # cast naar int
        while getal != 0:  # reeks eindigt wanneer 0 wordt ingegeven

            if (getal > 30 and getal % 5 == 0) or getal < 7:  # getal kleiner dan 30 die deelbaar zijn door 5 en getal kleiner dan 7
                som += getal  # tel op bij som
            getal = int(input("Geef een getal (0 om te eindigen): ")) # eindigt while loop
        print("De som van de getallen die aan de voorwaarde voldoet is " + str(som)) # print som in de while zodat hij elke keer opnieuw print en niet 1 keer op het einde


if __name__ == '__main__':
    main()
