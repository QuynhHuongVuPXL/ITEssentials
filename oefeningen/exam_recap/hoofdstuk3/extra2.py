leeftijd = int(input("Geef jouw leeftijd in: "))

if leeftijd < 12:
    prijs = 6
elif leeftijd < 18:
    prijs = 12.5
else:
    prijs = 25

print(f"Het lidgeld voor deze persoon van {leeftijd} is: {prijs}")