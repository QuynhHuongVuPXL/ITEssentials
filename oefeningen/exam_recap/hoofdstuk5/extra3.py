import random


def perfect_getal(getal):
    totaal_delers = 0

    for i in range(1, getal):
        if getal % i == 0:
            totaal_delers += i

    if totaal_delers == getal:
        return True
    else:
        return False


def random_getal():
    random_getal = random.randint(1, 100)
    random_perfect = perfect_getal(random_getal)
    print(f"Is {random_getal} een perfect getal? {random_perfect}")


def vier_getallen():
    lege_string = ""
    for i in range(4):
        random_getal = random.randint(1, 3)
        lege_string += str(random_getal)

    resultaat = int(lege_string)

    getal_perfect = perfect_getal(resultaat)
    print(f"Is {resultaat} een perfect getal? {getal_perfect}")


def main():
    getal = int(input("Geef een geheel getal in: "))

    getal_perfect = perfect_getal(getal)
    print(f"Is {getal} een perfect getal? {getal_perfect}")
    print

    random_getal()
    print()

    vier_getallen()


if __name__ == '__main__':
    main()
