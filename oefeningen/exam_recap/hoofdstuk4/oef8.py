langer_dan_een_uur = 0
index = 0
snelste_renner_tijd = 0
snelste_renner_naam = ""

nummer_renner = int(input("Geef nummer van de renner in: "))

while not nummer_renner < 0:
    tijd_in_seconden = int(input("Geef tijd in seconden van deze renner in: "))
    snelste_renner_tijd = tijd_in_seconden
    snelste_renner_naam = nummer_renner
    index += 1

    if tijd_in_seconden > 3600:
        langer_dan_een_uur += 1

    if tijd_in_seconden < snelste_renner_tijd:
        snelste_renner_tijd = tijd_in_seconden
        snelste_renner_naam = nummer_renner

    nummer_renner = int(input("Geef nummer van de renner in: "))

percentage_langer_dan_uur = langer_dan_een_uur / index * 100
print("Het percetnage dat er langer dan een uur over doet is " + str(percentage_langer_dan_uur))

minuten = snelste_renner_tijd // 60
seconden = snelste_renner_tijd % 60
uren = snelste_renner_tijd // 3600

print("De snelste renner is de renner met inschrijfnummer " + str(snelste_renner_naam))

print(str(uren) + " u " + str(minuten) + " min " + str(seconden) + " sec")
