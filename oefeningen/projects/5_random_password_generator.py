import random


def generate_password(password_length, special_characters):
    if password_length < 8 or password_length > 20:
        print("Password length must be at least 4 and less than 20.")
        return None

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*()_+-=[]{};':\",./<>?"

    password_characters = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    if special_characters == "yes":
        password_characters.append(random.choice(special))
        all_chars = lower + upper + digits + special
    else:
        all_chars = lower + upper + digits

    for i in range(password_length - len(password_characters)):
        password_characters.append(random.choice(all_chars))

    random.shuffle(password_characters)

    return "".join(password_characters)


def main():
    password_length = int(input("Enter the desired password length (minimum 8): "))
    special_characters = str(input("Include special characters (yes/no)?: "))

    password = generate_password(password_length, special_characters)

    if password:
        print(f"Generated password: {password}")


if __name__ == '__main__':
    main()
