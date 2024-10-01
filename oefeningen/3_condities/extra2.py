leeftijd = int(input("Geef jouw leeftijd in: "))

if leeftijd < 12:
    lidgeld = 6
elif leeftijd < 19:
    lidgeld = 12.5
else:
    lidgeld = 25

print(f"Het lidgeld voor deze persoon van {leeftijd} is: {lidgeld}")
