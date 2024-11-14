def hotel_kosten(aantal_nachten):
    hotel_kost_per_nacht = 140.50

    gratis_nachten = aantal_nachten // 3

    te_betalen_nachten = (aantal_nachten - 1) - gratis_nachten
    totale_hotel_kosten = hotel_kost_per_nacht * te_betalen_nachten

    return totale_hotel_kosten


def vliegtuig_kosten(stad):
    if stad == "Barcelona":
        return 183
    elif stad == "Rome":
        return 220
    elif stad == "Berlijn":
        return 450
    elif stad == "Oslo":
        return 450
    else:
        return "Ongeldige bestemming"


def huurauto_kosten(aantal_dagen):
    huurauto_kost_per_dag = 40

    totale_huurauto_kosten = huurauto_kost_per_dag * aantal_dagen

    if aantal_dagen > 7:
        totale_huurauto_kosten -= 50
    elif aantal_dagen > 3:
        totale_huurauto_kosten -= 30

    return totale_huurauto_kosten


def reis_kosten(stad, aantaldagen):
    totaal_hotel_kosten = hotel_kosten(aantaldagen)
    totaal_vliegtuig_kosten = vliegtuig_kosten(stad)

    if totaal_vliegtuig_kosten == "Ongeldige bestemming":
        return "Ongeldige bestemming ingevoerd"

    totale_huurauto_kosten = huurauto_kosten(aantaldagen)

    totale_prijs = totaal_hotel_kosten + totaal_vliegtuig_kosten + totale_huurauto_kosten

    return totale_prijs


def main():
    reisbestemming = str(input("Geef een reisbestemming in (Barcelona, Rome, Berlijn of Oslo): "))
    aantal_dagen = int(input("Geef het aantal dagen dat je in deze stad zal verblijven: "))

    kostprijs = reis_kosten(reisbestemming, aantal_dagen)

    print(f"De kostprijs van deze reis naar {reisbestemming} bedraagt {kostprijs} euro")


if __name__ == '__main__':
    main()
