som = 0
negatieve_getallen = 0
getal = int(input("Geef een geheel getal in: "))
while getal != 0:
    som += getal
    if getal < 0:
        negatieve_getallen += 1

    getal = int(input("Geef een geheel getal in: "))
print("De som van de ingegeven getallen is " + str(som))
print("Het aantal negatieve ingegeven getallen is " + str(negatieve_getallen))