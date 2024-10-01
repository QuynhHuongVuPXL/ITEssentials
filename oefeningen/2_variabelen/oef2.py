prijs_volwassenen = 11
prijs_kind = 6

aantal_volwassenen = int(input("Geef het aantal volwassenen in: "))
aantal_kinderen = int(input("Geef het aantal kinderen in: "))

totale_prijs = (prijs_volwassenen * aantal_volwassenen) + (prijs_kind * aantal_kinderen)

print("De totale prijs is " + str(totale_prijs))
