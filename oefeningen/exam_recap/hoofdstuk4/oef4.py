MAAN = 0.165
JUPUTER = 2.537
MARS = 0.378

for i in range(50, 121, 5):
    print("Aarde: " + str(i))
    print("Maan " + str(i * MAAN))
    print("Juputer " + str(i * JUPUTER))
    print("Mars " + str(i * MARS))
    print()
