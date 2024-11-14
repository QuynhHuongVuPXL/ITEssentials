getal = int(input("Geef een even getal in: "))
while getal % 2 != 0:
    getal = int(input("Foute ingave! Geef opnieuw een even getal in: "))

helft = getal / 2
for i in range(1, int(helft) + 1):
    print(i, "/", getal - i)

