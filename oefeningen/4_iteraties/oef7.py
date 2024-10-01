# hoogste_temperatuur = -100 # heel klein getal
hoogste_temperatuur = float("inf") # ook een heel klein getal

totaal = 0

for i in range(10):
    # temperatuur = int(input(f"Geef temperatuur van dag {i + 1} in: "))
    temperatuur = int(input("Geef temperatuur van de dag " + str(i+1) + " in: "))
    totaal += temperatuur

    if temperatuur > hoogste_temperatuur:
        hoogste_temperatuur = temperatuur

gemiddelde = totaal / 10
print("Het gemiddelde van de temperaturen is:", gemiddelde)
print("De hoogste temperatuur is:", float(hoogste_temperatuur))

# # kan ook de eerste input is het kleinste getal
# totaal = 0
# hoogste_temperatuur = 0
#
# temperatuur = int(input("Geef temperatuur van de dag 1 in: "))
# hoogste_temperatuur = temperatuur
# totaal += temperatuur
#
# for i in range(2, 11):
#     # temperatuur = int(input("Geef temperatuur van de dag " + str(i) + " in: "))
#     # totaal += temperatuur
#
#     if temperatuur > hoogste_temperatuur:
#         hoogste_temperatuur = temperatuur
#
#     temperatuur = int(input("Geef temperatuur van de dag " + str(i) + " in: "))
#     totaal += temperatuur




gemiddelde = totaal / 10

print("Het gemiddelde van de temperaturen is:", gemiddelde)
print("De hoogste temperatuur is:", float(hoogste_temperatuur))
