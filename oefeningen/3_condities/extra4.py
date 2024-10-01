naam = str(input("Geef naam van de speler in: "))
prijs_vorig_seizoen = int(input("Geef de prijs van vorig seizoen in: "))
leeftijd = int(input("Geef de leeftijd in: "))
beoordelingscijfer = int(input("Geef beoordelingscijfer in (0 - 10): "))
type_speler = str(input("Geef type van de speler in (A=Aanvaller; M=Middenvelder; V=verdediger; D=Doelman): "))
aantal_doelpunten = int(input("Geef het aantal doelpunten in: "))

basisprijs = prijs_vorig_seizoen

if leeftijd < 25:
    basisprijs *= 1.10
elif leeftijd > 30:
    basisprijs *= 0.95

if type_speler == "A":
    if aantal_doelpunten <= 5:
        basisprijs += 10000 * aantal_doelpunten
    else:
        basisprijs += 10000 * 5 + 20000 * (aantal_doelpunten - 5)
else:
    basisprijs += 10000 * beoordelingscijfer

if type_speler == "D" and aantal_doelpunten >= 20:
    basisprijs -= 9000 * (aantal_doelpunten - 21)

print(f"Naam: {naam}")
print(f"Prijs vorig seizoen: {float(prijs_vorig_seizoen)}")
print(f"Prijs nieuw seizoen: {basisprijs}")