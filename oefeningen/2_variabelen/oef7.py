lengte = float(input("Geef de lengte van het tapijt in (in meter): "))
breedte = float(input("Geef de breedte van het tapijt in (in meter): "))
prijs_per_vierkante_m = float(input("Geef de prijs per vierkante meter in: "))
plaatsingskosten_per_vierkante_m = float(input("Geef de plaatsingskosten per vierkante meter in: "))

kostprijs = lengte * breedte * prijs_per_vierkante_m
plaatsingskosten = lengte * breedte * plaatsingskosten_per_vierkante_m
totale_kosten = kostprijs + plaatsingskosten

print("De kostprijs van het tapijt is: " + str(kostprijs))
print("De plaatsingskosten van het tapijt zijn: " + str(plaatsingskosten))
print("De totale kost is: " + str(totale_kosten))
