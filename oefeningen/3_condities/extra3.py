# verbruik_per_m3 = int(input("Geef het verbruik per m3 in: "))
#
# VAST_RECHT = 25
#
# if verbruik_per_m3 <= 30:
#     prijs = VAST_RECHT
# elif verbruik_per_m3 <= 200:
#     prijs = 1 * (verbruik_per_m3 - 30) + VAST_RECHT
# elif verbruik_per_m3 <= 5000:
#     prijs = 1.15 * (verbruik_per_m3 - 30) + VAST_RECHT
# else:
#     prijs = 1.175 * (verbruik_per_m3 - 30) + VAST_RECHT
#
# print(f"De vebruikskosten van het geleverde water zijn: {prijs}")

# variant:
verbruik_per_m3 = int(input("Geef het verbruik per m3 in: "))

VAST_RECHT = 25

if verbruik_per_m3 <= 30:
    prijs = VAST_RECHT
elif verbruik_per_m3 <= 200:
    prijs = VAST_RECHT + (verbruik_per_m3 - 30) * 1
elif verbruik_per_m3 <= 5000:
    prijs = VAST_RECHT + (200 - 30) * 1 + (verbruik_per_m3 - 200) * 1.15
else:
    prijs = VAST_RECHT + (200 - 30) * 1 + (5000 - 200) * 1.15 + (verbruik_per_m3 - 5000) * 1.175


print(f"De vebruikskosten van het geleverde water zijn: {prijs}")
