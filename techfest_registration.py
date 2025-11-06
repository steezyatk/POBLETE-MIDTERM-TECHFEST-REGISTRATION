AUTHOR_NAME = "Jacob Catayoc"
AUTHOR_SECTION = "BTCS0"

def setup_registration():
    """Displays a welcome message and prompts for the number of participants."""
    print("Welcome to SMIT TechFest!")
    print(f"Event organized by {AUTHOR_NAME} of APPDAET {AUTHOR_SECTION}\n")

    try:
        num_participants = int(input("How many participants will register? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 0

    if num_participants <= 0:
        print("Invalid number of participants.")
        return 0

    return num_participants