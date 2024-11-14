# aantal_vlekken = int(input("Geef het aantal vlekken van Peppy in: "))
# dagen = 1
# totaal_aantal_druppels = 0
# while aantal_vlekken > 5 and dagen <= 7:
#     dagen += 1
#     som = int(aantal_vlekken / 2)
#     totaal_aantal_druppels += som
#     aantal_vlekken -= 2
#
# print("Het totaal aantal druppels is", totaal_aantal_druppels)


# alternatief
aantal_vlekken = int(input("Geef het aantal vlekken van Peppy in: "))
dagen = 1
totaal_aantal_druppels = 0
while aantal_vlekken > 5 and dagen <= 7:
    aantal_druppels = aantal_vlekken // 2
    totaal_aantal_druppels += aantal_druppels

    aantal_vlekken -= 2
    dagen += 1

print("Het totaal aantal druppels is", totaal_aantal_druppels)
