import random


def genereer_tekst(n):
    string = ""
    for tekens in range(n):
        random_letter = chr(random.randint(65, 90))
        string += random_letter
    print(string)


def main():
    aantal_tekens = int(input("Geef het aantal tekens in: "))

    genereer_tekst(aantal_tekens)


if __name__ == '__main__':
    main()
