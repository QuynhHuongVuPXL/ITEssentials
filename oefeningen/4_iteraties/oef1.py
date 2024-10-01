# # for loop
# gewicht_per_stuk = int(input("Geef het gewicht van een appel in: "))
# for i in range(1, 101):
#     gewicht = gewicht_per_stuk * 1
#     print(f"{i} appel(s) = {gewicht * i} gr.")

# while loop
gewicht_per_stuk = int(input("Geef het gewicht van een appel in: "))
totaal_appels = 1
while(totaal_appels < 101):
    gewicht = gewicht_per_stuk * 1
    print(f"{totaal_appels} appel(s) = {gewicht * totaal_appels} gr.")
    totaal_appels += 1

