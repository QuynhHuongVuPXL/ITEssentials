hoogte = int(input("Geef de hoogte van de driehoek in: "))
for i in range(hoogte):
    for j in range(hoogte - i):
        print("@", end="")
    print()
