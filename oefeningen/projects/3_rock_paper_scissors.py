import random


def fight(choice, computer_choice):
    if (choice == 1 and computer_choice == "Rock") or (choice == 2 and computer_choice == "Paper") or (choice == 3 and computer_choice == "Scissor"):
        return "<== It's a tie! =>"
    elif (choice == 1 and computer_choice == "Paper") or (choice == 2 and computer_choice == "Scissor") or (choice == 3 and computer_choice == "Rock"):
        return "<== Computer wins! =>"
    else:
        return "<== You win! =>"


def main():
    computer_hand = ["Rock", "Paper", "Scissor"]

    print(
        "Winning rules of the game ROCK PAPER SCISSORS are:\nRock vs Paper -> Paper wins\nRock vs Scissors -> Rock wins\nPaper vs Scissors -> Scissors wins ")
    print()

    play_again = "y"

    while play_again != "n":
        print("Pick one of the choices: ")
        for i in range(len(computer_hand)):
            print(f"{i + 1} - {computer_hand[i]}")

        choice = int(input("Enter your choice "))
        while choice not in [1, 2, 3]:
            choice = int(input("Enter a valid choice "))

        my_hand = computer_hand[choice - 1]
        computer_choice = random.choice(computer_hand)

        print(f"User choice is: {my_hand} ")
        print("Now it's the Computer's turn...")
        print(f"Computer choice is: {computer_choice} ")
        print(f"{my_hand} vs {computer_choice}")

        output = fight(choice, computer_choice)
        print(output)
        print()

        play_again = str(input("Do you want to play again? (Y/N) ").lower())

    print("Thanks for playing!")


if __name__ == '__main__':
    main()