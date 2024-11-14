leeftijd = int(input("Geef jouw leeftijd in: "))
aansluitingsjaar = int(input("Geef jouw aansluitingsjaar bij de club in: "))

JAAR_NU = 2023
BASISBEDRAG = 100

if leeftijd < 21 or leeftijd > 60:
    BASISBEDRAG -= 14.5

aangesloten_jaar = JAAR_NU - aansluitingsjaar
reductie_aangesloten_jaar = aangesloten_jaar * 2.5
BASISBEDRAG -= reductie_aangesloten_jaar

if BASISBEDRAG < 62.5:
    BASISBEDRAG = 62.5

print("De bijdrage voor dit lid is: " + str(BASISBEDRAG))
