import random


def main():
    name = str(input("What is your name? "))
    print(
        "Hello, " + name + "! \nWelcome to guess-the-norwegian-word game!\nYou have 12 attempts to guess the word correctly.\nIf you guess a letter right, then a turn won't be deducted.\nYou might have to use Norwegian letters.\nGoodluck")
    print()

    words = ["pølse", "huset", "fiske", "skole", "solen", "månen", "blått", "sove", "biler", "gulvt",
             "smake", "drømm", "stove", "væske", "krone", "grønn", "mange", "farge", "bokse", "stille",
             "brann", "kirse", "sverd", "vindu", "baker", "guler", "stein", "hybel", "drage", "søker"]

    word = random.choice(words).lower()
    print(word)

    print("The word has " + str(len(word)) + " letters.")
    guesses = ""
    turns = 12

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print()
            print()
            print("You win!")
            print("The word is: ", word)
            break

        print()
        guess = input("Guess a character: ").lower()
        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong character.")
            print("You have " + str(turns) + " more guesses.")

        if turns == 0:
            print("You lose.")


if __name__ == '__main__':
    main()
