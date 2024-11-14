sterren = int(input("Geef het aantal sterren in (1 - 5): "))
code = str(input("Geef de code in (O=enkel ontbijt; H=half-pension; V=vol pension; A=all-incl): "))
aantal_overnachtingen = int(input("Geef het aantal overnachtingen in: "))
seizoen = str(input("Geef het seizoen in (H=hoogseizoen; L=laagseizoen; T=tussenseizoen): "))

kosten_per_nacht = 0
if sterren == 1:
    kosten_per_nacht = 30
elif sterren == 2 or sterren == 3:
    kosten_per_nacht = 40
elif sterren == 4 or sterren == 5:
    kosten_per_nacht = 55

overnachtings_kosten = kosten_per_nacht * aantal_overnachtingen

maaltijd_kosten = 0
if code == "O":
    maaltijd_kosten = 0.20 * overnachtings_kosten
elif code == "H":
    maaltijd_kosten = 0.50 * overnachtings_kosten
elif code == "V":
    maaltijd_kosten = 0.60 * overnachtings_kosten
elif code == "A":
    maaltijd_kosten = 0.60 * overnachtings_kosten + (aantal_overnachtingen * 80)

totaal_prijs = overnachtings_kosten + maaltijd_kosten

if seizoen == "L" and (code == "O" or code == "H"):
    totaal_prijs *= 0.90


print("De prijs voor de vakantie van deze persoon is: " + str(totaal_prijs))