totaal_premie = 0
hoogste_premie = 0
familienaam = str(input("Geef jouw familienaam in: "))

while familienaam != "/" and familienaam != "*":
    premie = 0
    voornaam = str(input("Geef jouw voornaam in: "))
    aantal_dienstjaren = int(input("Geef het aantal dienstjaren in: "))

    while not 0 <= aantal_dienstjaren <= 40:
        aantal_dienstjaren = int(input("Geef een juist aantal dienstjaren in (tussen 0 en 40)): "))

    if aantal_dienstjaren >= 5:
        premie = aantal_dienstjaren * 25

    totaal_premie += premie

    if premie > hoogste_premie:
        hoogste_premie = premie

    print(f"voornaam = {voornaam}\nfamilienaam = {familienaam}\naantal dienstjaren = {aantal_dienstjaren}\npremie = {premie}")

    familienaam = str(input("Geef jouw familienaam in: "))

print(f"De totaal te betalen premie is {totaal_premie}")
print(f"De hoogste premie is {hoogste_premie}")