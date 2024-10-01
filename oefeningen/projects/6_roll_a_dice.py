import random

roll_a_dice = str(input("Do you want to roll a dice? (yes / no) ").lower())

if roll_a_dice == "yes":
    rolled_dice = random.randint(1, 6)
    print(f"You rolled a {rolled_dice}")
else:
    print("Bye")