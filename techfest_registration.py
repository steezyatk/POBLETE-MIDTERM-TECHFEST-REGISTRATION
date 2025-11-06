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


# --- Task 5: Track Summary Report ---
def track_summary_report(participants):
    """Counts participants per track and prints a summary."""
    track_counts = {}

    for p in participants:
        track = p["track"]
        # Increment count for the track, or set to 1 if first time
        track_counts[track] = track_counts.get(track, 0) + 1

    print("\nParticipants per track:")
    # Print summary, sorted by track name for consistency
    for track, count in sorted(track_counts.items()):
        print(f"{track}: {count}")


# Main execution logic
def main():
    num_participants = setup_registration()

    if num_participants > 0:
        # Task 2
        participants = collect_participants(num_participants)

        # Make a commit for Task 2
        # git commit -m "Implemented participant registration"

        # Task 3
        unique_tracks = track_diversity_report(participants)

        # Make a commit for Task 3
        # git commit -m "Added track diversity analysis"

        # Task 4
        duplicate_name_detection(participants)

        # Make a commit for Task 4
        # git commit -m "Implemented duplicate name detection"

        # Task 5
        track_summary_report(participants)

        # Make a commit for Task 5
        # git commit -m "Implemented track summary report"


if __name__ == "__main__":
    main()
