gewicht = float(input("Vul in gewicht: "))
lengte = float(input("Vul in lengte: "))

bmi = gewicht / (lengte * lengte)

if bmi < 18:
    resultaat = "ondergewicht"
elif bmi < 25:
    resultaat = "ok"
elif bmi < 30:
    resultaat = "overgewicht"
elif bmi < 40:
    resultaat = "obesitas"
else:
    resultaat = "ziekelijk overgewicht"

print(f"BMI: {resultaat}")