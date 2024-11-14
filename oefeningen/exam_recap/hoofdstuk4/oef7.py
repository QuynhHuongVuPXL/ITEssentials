som = 0

temperatuur = float(input("Geef temperatuur van dag 1 in: "))
hoogste_temperatuur = temperatuur
som += temperatuur

for dag in range(2, 11):
    temperatuur = float(input("Geef temperatuur van dag " + str(dag) + " in: "))
    som += temperatuur
    if temperatuur > hoogste_temperatuur:
        hoogste_temperatuur = temperatuur

gemiddelde = som / 10
print("Het gemiddelde: " + str(gemiddelde))
print("De hoogste temperatuur is " + str(hoogste_temperatuur))