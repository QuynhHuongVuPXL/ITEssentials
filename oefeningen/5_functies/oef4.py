import random


def genereer_random_getal():
    return random.randint(1, 10)


def genereer_feedback(ingegeven_getal, random_getal):
    if ingegeven_getal < random_getal:
        print("hoger")
    else:
        print("lager")


def main():
    random_getal = genereer_random_getal()
    # print(random_getal)

    aantal_beurten = 4

    while aantal_beurten > 0:
        ingegeven_getal = int(input("Geef een getal in: "))

        if random_getal == ingegeven_getal:
            print("Proficiat, het getal is geraden")
            aantal_beurten = 0
        elif aantal_beurten == 0:
            print("Je 4 beurten zijn voorbij")
        elif aantal_beurten >= 0:
            genereer_feedback(ingegeven_getal, random_getal)

        aantal_beurten -= 1


if __name__ == '__main__':
    main()
