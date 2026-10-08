def ask_user_info():
    while True:
        try:
            user_age = int(input("What is your age? "))
            if int(user_age) < 12:
                print("You are too young.")
                raise SystemExit
            else:
                print("You are old")
            break
        except ValueError:
            print("Error: given value is not an integer. Try again.")
    username = str(input("What is your name? "))
    return username, user_age
    