username = input("What is your name? ")
user_age = input("What is your age? ")

print(f"Your name is {username} and your age is {user_age}. Is this correct? (yes/no)")
if input().lower() == "yes":
    if int(user_age) < 12:
        print("You are too young.")
        raise SystemExit
    else:
        print("Welcome.")

while True:
    print("\nNew Game")
    print("Load Game")
    print("Settings")
    print("Quit")
    input_choice = input("\nEnter an option: ")
    if input_choice.lower() == "quit":
        raise SystemExit
    elif input_choice.lower() == "new game":
        print("Starting a new game...")
    elif input_choice.lower() == "load game":
        print("Loading game...")
    elif input_choice.lower() == "settings":
        print("Opening settings...")