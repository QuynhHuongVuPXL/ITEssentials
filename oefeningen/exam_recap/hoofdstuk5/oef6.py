import random


def main():
    for i in range(1, 6):
        print("reeks " + str(i))
        for j in range(1, 6):
            nummer1 = random.randint(0, 20)
            nummer2 = random.randint(nummer1, 20)
            print(f"{j}) {nummer2} - {nummer1} = ")
        print()


if __name__ == '__main__':
    main()
