# gewicht = int(input("Geef het gewicht van een appel in: "))
# for i in range(1, 101):
#     print(str(i) + " appel(s) = " + str(i * gewicht) + " gr.")


gewicht = int(input("Geef het gewicht van een appel in: "))
appels = 1
while appels < 101:
    print(str(appels) + " appels(s) = " + str(appels * gewicht) + " gr.")

    appels += 1
