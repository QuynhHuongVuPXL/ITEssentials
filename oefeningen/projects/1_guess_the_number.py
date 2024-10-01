import random


def main():
    total_chances = 7

    name = str(input("What is your name? "))
    print("Welcome " + name + " to the guess-the-number game!")

    min_number = int(input("Enter lower bound: "))
    max_number = int(input("Enter upper bound: "))

    while max_number <= min_number:
        print(f"The upper bound must be greater than the lower bound ({min_number}).")
        max_number = int(input("Enter upper bound: "))

    print("Great! You need to guess a number between " + str(min_number) + " and " + str(
        max_number) + ", you only have 7 chances.\nGoodluck!")

    random_number = random.randint(min_number, max_number)
    print(random_number)

    initial_chances = total_chances

    while total_chances > 0:
        guess = int(input("Please enter your guess: "))

        if guess == random_number:
            guessed_used = initial_chances - total_chances + 1
            print("Congratulations! You guessed the number in " + str(guessed_used) + " guesses!")
            break
        elif guess < random_number:
            print("Try again! You guessed too small.")
        elif guess > random_number:
            print("Try again! You guess too high")

        total_chances -= 1
        print("You have " + str(total_chances) + " chances left.")

        if total_chances == 0:
            print("Better luck next time! The correct number was " + str(random_number))



if __name__ == '__main__':
    main()
