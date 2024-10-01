# jaartal = int(input("Geef jaartal van de film in: "))
# rating = int(input("Geef rating van de film in: "))
#
# basisprijs = 5
# jaar_nu = 2023
# if jaar_nu - jaartal < 2:
#     basisprijs += 1
#
# if rating == 4 or rating == 5:
#     basisprijs += 2
#
# print("De prijs van een film is " + str(basisprijs))

# uitbreiding
jaartal = int(input("Geef jaartal van de film in: "))
rating = int(input("Geef rating van de film in: "))

BASISPRIJS = 5
prijs = 0
jaar_nu = 2023

if jaar_nu - jaartal < 2:
    prijs = 1

if rating == 4 or rating == 5:
    prijs = 2
elif rating == 2 or rating == 3:
    prijs = 1

totaal_prijs = BASISPRIJS + prijs

if totaal_prijs > 7:
    totaal_prijs = 7

print("De prijs van een film is " + str(totaal_prijs))