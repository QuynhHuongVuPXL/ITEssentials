HUIDIGE_JAAR = 2023
basisbedrag = 100

leeftijd = int(input("Geef jouw leeftijd in: "))
aansluitingsjaar = int(input("Geef jouw aansluitingsjaar bij de club in: "))

if leeftijd < 21 or leeftijd > 60:
    basisbedrag -= 14.50

reductie_jaar = HUIDIGE_JAAR - aansluitingsjaar
bedrag_reductie_jaar = reductie_jaar * 2.5
basisbedrag -= bedrag_reductie_jaar

if basisbedrag <= 62.5:
    basisbedrag = 62.5

print(f"De bijdrage voor dit lid is: " + str(basisbedrag))
