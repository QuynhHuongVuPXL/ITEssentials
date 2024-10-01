afstand = int(input("Geef de afsand van de vlucht in (in km): "))
klasse = int(input("Geef de klasse van de vlucht in (1=toeristenklasse;2=charter;3=zakenreis): "))

prijs = 0

if afstand < 1000:
    prijs += afstand * 0.25
elif afstand < 3000:
    prijs += afstand * 0.20
else:
    prijs += afstand * 0.12

if klasse == 2:
    prijs *= 0.80
elif klasse == 3:
    prijs *= 1.30

print(f"De prijs van jouw ticket is {prijs} euro")


