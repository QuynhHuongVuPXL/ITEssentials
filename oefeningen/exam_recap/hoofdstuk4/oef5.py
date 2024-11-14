getal = int(input("Geef een getal tussen 1 en 100 in (= grenzen inclusief): "))

while not 1 < getal < 100:
    if getal <= 1:
        print("Foute ingave! Het getal moet groter zijn dan 1!")

    if getal >= 100:
        print("Foute ingave! Het getal moet kleiner zijn dan 100!")

    getal = int(input("Geef een getal tussen 1 en 100 in (= grenzen inclusief): "))
print("Het correct ingegeven getal is " + str(getal))
