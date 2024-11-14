def main():
    getallenlijst = []
    totaal = 0
    aantal_onder_gemiddelde = 0
    LENGTE = 15

    for i in range(LENGTE):
        getal = int(input(f"Geef geheel getal {i + 1} in: "))
        getallenlijst.append(getal)

    for getal in getallenlijst:
        totaal += getal

    gemiddelde = totaal / LENGTE

    for getal in getallenlijst:
        if getal < gemiddelde:
            aantal_onder_gemiddelde += 1

    percentage_onder_gemiddelde = aantal_onder_gemiddelde / LENGTE * 100

    print(f"Gemiddelde: {round(gemiddelde, 1)}")
    print(f"Aantal onder gemiddelde: {aantal_onder_gemiddelde}")
    print(f"Percentage onder gemiddelde: {round(percentage_onder_gemiddelde, 1)}")


if __name__ == '__main__':
    main()
