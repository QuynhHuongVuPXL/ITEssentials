def main():
    productkost = int(input("geef de productkost in "))
    som = 0
    totaal_product = 0
    while productkost > 0 and totaal_product <= 9:
        som += productkost
        totaal_product += 1

        if totaal_product < 9:
            productkost = int(input("geef de productkost in "))

    if totaal_product > 0:
        gemiddelde = som / totaal_product
        print(gemiddelde)


if __name__ == '__main__':
    main()