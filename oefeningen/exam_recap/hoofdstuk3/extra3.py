# verbruik = int(input("Geef het verbruik per m3 in: "))
#
# VAST_RECHT = 25
#
# if verbruik <= 30:
#     prijs = VAST_RECHT
# elif verbruik <= 200:
#     prijs = 1 * (verbruik - 30) + VAST_RECHT
# elif verbruik <= 5000:
#     prijs = 1.15 * (verbruik - 30) + VAST_RECHT
# else:
#     prijs = 1.175 * (verbruik - 30) + VAST_RECHT
#
# print(f"De vebruikskosten van het geleverde water zijn: {prijs}")

# variant
verbruik = int(input("Geef het verbruik per m3 in: "))

VAST_RECHT = 25

if verbruik <= 30:
    prijs = VAST_RECHT
elif verbruik <= 200:
    prijs = VAST_RECHT + (verbruik - 30) * 1
elif verbruik <= 5000:
    prijs = VAST_RECHT + (200 - 30) * 1 + (verbruik - 200) * 1.15
else:
    prijs = VAST_RECHT + (200 - 30) * 1 + (5000 - 200) * 1.15 + (verbruik - 5000) * 1.175

print(f"De vebruikskosten van het geleverde water zijn: {prijs}")
