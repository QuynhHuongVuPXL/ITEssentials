brutoloon = float(input("Geef het bruto loon in: "))
vakantiegeld = brutoloon * 0.05

if vakantiegeld >= 350:
    jaarlijkse_bijdrage = 350 * 0.08
else:
    jaarlijkse_bijdrage = vakantiegeld * 0.08

print("Het bruto loon van deze werknemer is " + str(brutoloon))
print("Het vakantiegeld van deze werknemer is " + str(vakantiegeld))
print("De jaarlijkse bijdrage van deze werkenmer is " + str(jaarlijkse_bijdrage))