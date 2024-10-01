def main():
    email = "InterviewBit@gmail.com"

    email_split = email.split("@")

    print(f"Your username is {email_split[0]} & domain is {email_split[-1]}")



if __name__ == '__main__':
    main()