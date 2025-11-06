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

def track_diversity_report(participants):
    """Identifies and displays unique tracks, checking for variety."""
    unique_tracks = set(p["track"] for p in participants)

    if unique_tracks:
        print("\nTracks offered in this event:")
        print(", ".join(sorted(unique_tracks))) # Sorted for consistent display
        if len(unique_tracks) < 2:
            print("Not enough variety in tracks.")
    else:
        # This case shouldn't happen if num_participants > 0, but good for robustness
        print("\nNo tracks were registered.")

    return unique_tracks

