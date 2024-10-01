getala = int(input("Geef geheel getal a in: "))
getalb = int(input("Geef geheel getal b in: "))
code = int(input("Geef code in (1=optelling;2=aftrekking;3=vermenigvuldiging;4=kwadraat van a;5=kwadraat van b): "))

if code == 1:
    resultaat = getala + getalb
elif code == 2:
    resultaat = getala - getalb
elif code == 3:
    resultaat = getala * getalb
elif code == 4:
    resultaat = getala ** 2
elif code == 5:
    resultaat = getalb ** 2
else:
    resultaat = "foutieve code"

print(f"De 2 getallen zijn {getala} en {getalb} en het resultaat is {resultaat}")
