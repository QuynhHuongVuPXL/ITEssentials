langer_dan_een_uur = 0
totaal_renners = 0
snelste_renner_nummer = 0
snelste_renner_tijd = 100000

nummer = int(input("Geef nummer van de renner: "))

while not nummer <= 0:
    tijd_in_seconden = int(input("Geef tijd in seconden van deze renner in: "))
    totaal_renners += 1
    if tijd_in_seconden < snelste_renner_tijd:
        snelste_renner_tijd = tijd_in_seconden
        snelste_renner_nummer = nummer

    if tijd_in_seconden > 3600:
        langer_dan_een_uur += 1

    nummer = int(input("Geef nummer van de renner: "))

percentage_langer_dan_een_uur = langer_dan_een_uur / totaal_renners * 100

print("Het percentage renners dat er langer dan een uur over doet is", percentage_langer_dan_een_uur)
print("De snelste renner is de renner met inschrijfnummer", snelste_renner_nummer)

uren = snelste_renner_tijd // 3600
# kan ook uren = int(snelste_renner_tijd / 3600)
minuten = snelste_renner_tijd // 60
# minuten = int((snelste_renner_tijd%3600)/60)
seconden = snelste_renner_tijd % 60
# seconden = (snelste_renner_tijd%3600)%60
print(uren, "u", minuten, "min", seconden, "sec")
