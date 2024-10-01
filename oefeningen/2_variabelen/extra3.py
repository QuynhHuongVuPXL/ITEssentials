diameter = int(input("Geef de diameter van je wiel in (inches): "))
afstand = float(input("Geef de afstand die je wil afleggen (m): "))

omwenteling_in_inches = diameter * 3.14159
omwenteling_in_meters = omwenteling_in_inches * 0.0254
omwenteling_voor_afstand = afstand / omwenteling_in_meters

print("De afgelegde weg van een omwenteling in inches is: " + str(omwenteling_in_inches))
print("De afgelegde weg van een omwenteling in meters is: " + str(omwenteling_in_meters))
print("Het aantal omwentelingen dat je wiel moet maken om " + str(afstand) + " meter af te leggen is: " + str(omwenteling_voor_afstand))