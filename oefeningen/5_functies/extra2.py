def omzetten_tijdstip(in_uur, in_min, uit_uur, uit_min):
    totaal_min_in = in_uur * 60 + in_min
    totaal_min_uit = uit_uur * 60 + uit_min

    aanwezigheidsduur = totaal_min_uit - totaal_min_in

    return aanwezigheidsduur


def gemiddelde_aanwezigheids_in_uren_en_minuten(gemiddelde_minuten):
    uren = gemiddelde_minuten // 60
    minuten = gemiddelde_minuten % 60

    print(f"Gemiddelde duur binnen = {uren} en {minuten} minuten")


def main():
    aantal_bezoekers = 0
    bezoekers_meer_dan_een_uur = 0
    totale_tijd_iedereen = 0

    in_uur = int(input("Geef het uur van binnen komen: "))

    while in_uur != 0:

        in_min = int(input("Geef de minuten van binnen komen: "))
        uit_uur = int(input("Geef het uur van weggaan: "))
        uit_min = int(input("Geef de minuten van weggaan: "))

        totale_duur = omzetten_tijdstip(in_uur, in_min, uit_uur, uit_min)

        if totale_duur > 60:
            bezoekers_meer_dan_een_uur += 1

        totale_tijd_iedereen += totale_duur
        aantal_bezoekers += 1

        in_uur = int(input("Geef het uur van binnen komen: "))

    print(f"Er waren {bezoekers_meer_dan_een_uur} bezoekers meer dan 1 uur binnen")

    gemiddelde = totale_tijd_iedereen / aantal_bezoekers

    gemiddelde_aanwezigheids_in_uren_en_minuten(gemiddelde)

if __name__ == '__main__':
    main()
