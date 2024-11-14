import random
def selecteer_uitlijst(lijst, aantal):
    hulp = []
    for i in range(aantal):
        index = random.randrange(len(lijst))
        while lijst[index] in hulp:
            index = random.randrange(len(lijst))
        hulp.append(lijst[index])
    return hulp


def main():
    sporten = ["voetbal", "tennis", "badminton", "schaak", "league of legends", "ultimate frisbee", "petanque"]
    print(selecteer_uitlijst(sporten, 4))



if __name__ == '__main__':
    main()