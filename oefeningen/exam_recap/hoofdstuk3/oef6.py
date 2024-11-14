# jaartal = int(input("Geef jaartal van de film in: "))
# rating = int(input("Geef rating van de film in (1 - 5): "))
#
# prijs = 0
# JAAR_NU = 2023
# BASISPRIJS = 5
# prijs += BASISPRIJS
#
# if JAAR_NU - jaartal < 2:
#     prijs += 1
#
# if rating >= 4:
#     prijs += 2
#
# print("De prijs van een film is: " + str(prijs))

# uitbreiding
jaartal = int(input("Geef jaartal van de film in: "))
rating = int(input("Geef rating van de film in (1 - 5): "))

prijs = 0
JAAR_NU = 2023
BASISPRIJS = 5
prijs += BASISPRIJS

if JAAR_NU - jaartal < 2:
    prijs += 1

if rating == 4 or rating == 5:
    prijs += 2
elif rating == 3 or rating == 2:
    prijs += 1

if prijs > 7:
    prijs = 7

print("De prijs van een film is: " + str(prijs))
