totaal_premie = 0
hoogste_premie = 0

familienaam = str(input("Geef jouw familienaam in: "))
while familienaam != "/" and familienaam != "*":
    voornaam = str(input("Geef jouw voornaam in: "))
    dienstjaren = int(input("Geef het aantal dienstjaren in: "))

    while not 0 < dienstjaren < 40:
        dienstjaren = int(input("Geef het aantal dienstjaren in: "))

    premie = dienstjaren * 25

    if dienstjaren < 5:
        premie = 0

    totaal_premie += premie

    if premie > hoogste_premie:
        hoogste_premie = premie

    print("familienaam " + str(familienaam))
    print("voornaam " + str(voornaam))
    print("premie " + str(premie))

    familienaam = str(input("Geef jouw familienaam in: "))

print("De totaal te betalen premie is " + str(totaal_premie))
print("De hoogste premie is " + str(hoogste_premie))
