import random


def main():
    for i in range(5):
        print(f"reeks {i + 1}")
        for j in range(5):
            random_eerste_getal = random.randint(0, 20)
            random_tweede_getal = random.randint(0, random_eerste_getal)

            print(f"{j + 1}) {random_eerste_getal} - {random_tweede_getal} =")
        print()


if __name__ == '__main__':
    main()
