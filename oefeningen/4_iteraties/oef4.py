GEWICHT_MAAN = 0.165
GEWICHT_JUPITER = 2.537
GEWICHT_MARS = 0.378

for i in range(50, 121, 5):
    aarde = i
    maan = aarde * GEWICHT_MAAN
    jupiter = aarde * GEWICHT_JUPITER
    mars = aarde * GEWICHT_MARS

    print("Aarde:", aarde)
    print("Maan:", maan)
    print("Jupiter:", jupiter)
    print("Mars:", mars)
    print()
