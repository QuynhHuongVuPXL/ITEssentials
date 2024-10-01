sterren = int(input("Geef het aantal sterren in (1 - 5): "))
code = str(input("Geef de code in (O=enkel ontbijt; H=half-pension; V=vol pension; A=all-incl): "))
aantal_overnachtingen = int(input("Geef het aantal overnachtingen in: "))
seizoen = str(input("Geef het seizoen in (H=hoogseizoen; L=laagseizoen; T=tussenseizoen): "))

kosten_per_nacht = 0
if sterren == 1:
    kosten_per_nacht = 30
elif sterren <= 3:
    kosten_per_nacht = 40
else:
    kosten_per_nacht = 55

overnachtings_kosten = kosten_per_nacht * aantal_overnachtingen

maaltijd_kosten = 0
if code == "O":
    maaltijd_kosten = overnachtings_kosten * 0.20
elif code == "H":
    maaltijd_kosten = overnachtings_kosten * 0.50
elif code == "V":
    maaltijd_kosten = overnachtings_kosten * 0.60
else:
    maaltijd_kosten = overnachtings_kosten * 0.60 + (aantal_overnachtingen * 80)

totaal_prijs = overnachtings_kosten + maaltijd_kosten

if seizoen == "L" and (code == "O" or code == "H"):
    totaal_prijs *= 0.90

print(f"De prijs voor de vakantie van deze persoon is: {totaal_prijs}")
