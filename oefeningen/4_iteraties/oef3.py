som = 0
aantal_negatieve_getallen = 0

getal = int(input("Geef een geheel getal in: "))

while getal != 0:
    som += getal

    if getal < 0:
        aantal_negatieve_getallen += 1

    getal = int(input("Geef een geheel getal in: "))

print()
print("De som van de ingegeven getallen is:", som)
print("Het aantal negatieve ingegeven getallen is:", aantal_negatieve_getallen)
