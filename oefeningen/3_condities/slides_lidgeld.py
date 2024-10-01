burgelijke_staat = int(input("Geef burgelijke staat (1 = ongehuwd; 2 = gehuwd; 3 = weduw(e)): "))
leeftijd = int(input("Geef leeftijd: "))

# programma 1
if burgelijke_staat == 1:
    lidgeld = 25
elif burgelijke_staat == 2:
    lidgeld = 20
else:
    lidgeld = 15

# # programma 2
# if burgelijke_staat == 1 and leeftijd < 30:
#     lidgeld = 25
# else:
#     lidgeld = 15
#
# # programma 3
# if leeftijd < 30 and burgelijke_staat == 1:
#     lidgeld = 25
# else:
#     lidgeld = 15
#
# # programma 4
# if burgelijke_staat == 1:
#     lidgeld = 25
# elif burgelijke_staat == 2 and leeftijd < 30:
#     lidgeld = 20
# else:
#     lidgeld = 15

print(f"Je betaalt {lidgeld} euro")