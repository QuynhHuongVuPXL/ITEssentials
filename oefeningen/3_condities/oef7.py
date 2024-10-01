resultaat1 = int(input("Geef resultaat 1 in: "))
resultaat2 = int(input("Geef resultaat 2 in: "))
resultaat3 = int(input("Geef resultaat 3 in: "))

percentage = ((resultaat1 + resultaat2 + resultaat3) / 60) * 100

if percentage < 60:
    graad = "onvoldoende"
elif percentage < 70:
    graad = "voldoende"
elif percentage < 80:
    graad = "onderscheiding"
elif percentage < 90:
    graad = "grote onderscheiding"
else:
    graad = "grootste onderscheiding"

print(f"Het percentage van deze student is {percentage} en zijn graad is {graad}")