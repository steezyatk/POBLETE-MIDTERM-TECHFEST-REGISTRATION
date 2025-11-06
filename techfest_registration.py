# --- Task 1: Registration Setup ---
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
# --- Task 2: Collect Participant Information ---
def collect_participants(num_participants):
    """Collects participant names and chosen tracks."""
    participants = []
    for i in range(num_participants):
        print(f"\n--- Participant {i+1} ---")
        name = input("Enter participant name: ")
        track = input("Enter chosen track: ")

        participant_record = {
            "name": name,
            "track": track
        }
        participants.append(participant_record)

    print("\nRegistered Participants:")
    for i, p in enumerate(participants):
        print(f"{i+1}. {p['name']} - {p['track']}")

    return participants
# --- Task 3: Track Diversity Report ---
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
# --- Task 4: Duplicate Name Detection ---
def duplicate_name_detection(participants):
    """Checks and reports on any duplicate participant names."""
    names_seen = set()
    duplicate_names = set()

    for p in participants:
        name = p["name"]
        if name in names_seen:
            duplicate_names.add(name)
        names_seen.add(name)

    print()
    if duplicate_names:
        for name in sorted(duplicate_names): # Sorted for consistent display
            print(f"Duplicate name found: {name}")
    else:
        print("No duplicate names.")
