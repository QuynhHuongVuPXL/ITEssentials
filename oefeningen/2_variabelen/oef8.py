afgelegde_km = int(input("Geef het aantal afgelegde km per jaar: "))
verbruik = float(input("Geef het verbruik in liter per 100 km in : "))
prijs_per_liter = float(input("Geef de prijs per liter in: "))

totale_kosten = (afgelegde_km * verbruik * prijs_per_liter) / 100
print("De totale kosten per jaar voor het opgegeven aantal km is: " + str(totale_kosten))

kostprijs = (verbruik * prijs_per_liter) / 100
print("De kostprijs per km rijden is: " + str(kostprijs))