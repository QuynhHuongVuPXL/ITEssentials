# def kwadraat(a):
#     return a * a
#
#
# def som_van_kwadraten(x, y):
#     print( kwadraat(x) + kwadraat(y))
#
#
# print(kwadraat(10))
# som_van_kwadraten(10, 10)

#
# totaal_minuten = int(input("Geef het aantal minuten: "))
#
# uren = totaal_minuten // 60
# minuten = totaal_minuten % 60
# seconden = minuten * 60
#
# print(f"Uren: {uren}, Minuten: {minuten}, Seconden: {seconden}")

totaal_uren = float(input("Geef het aantal uren: "))

uren = int(totaal_uren)
minuten = int((totaal_uren - uren) * 60)
seconden = int(((totaal_uren - uren) * 60 - minuten) * 60)

print(f"Uren: {uren}, Minuten: {minuten}, Seconden: {seconden}")
