getal = int(input("Geef getal in: "))
tabel = int(input("Geef grootte tabel: "))

for x in range(1, tabel + 1):
    print(x, "x", getal, "=", x * getal)
