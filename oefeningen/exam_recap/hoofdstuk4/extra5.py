eerste_nummer = 1
tweede_nummer = 1

print(eerste_nummer, end=" ")
print(tweede_nummer, end=" ")

for i in range(1500):
    volgende_nummer = eerste_nummer + tweede_nummer
    eerste_nummer = tweede_nummer
    tweede_nummer = volgende_nummer

    if volgende_nummer < 1500:
        print(volgende_nummer, end=" ")
