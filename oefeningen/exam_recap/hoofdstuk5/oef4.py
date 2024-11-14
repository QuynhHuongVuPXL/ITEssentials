import random


def main():
    random_getal = random.randint(1, 10)
    print(random_getal)

    aantal_beurten = 0

    getal = int(input("Geef een getal in: "))
    aantal_beurten += 1

    while getal != random_getal and aantal_beurten != 4:
        aantal_beurten += 1
        if getal < random_getal:
            print("hoger")

        if getal > random_getal:
            print("lager")

        if getal == random_getal:
            aantal_beurten = 4

        getal = int(input("Geef een getal in: "))

    if aantal_beurten == 4 and getal != random_getal:
        print("je 4 beurten zijn voorbij")
    else:
        print("proficiat, het getal is geraden")


if __name__ == '__main__':
    main()
