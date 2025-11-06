# Replace YOUR NAME and YOUR SECTION
AUTHOR_NAME = "Poblete"
AUTHOR_SECTION = "BTCS2"

def setup_registration():
    print("Welcome to SMIT TechFest!")
    print(f"Event organized by {AUTHOR_NAME} of APPDAET {AUTHOR_SECTION}\n")

    try:
        num_participants = int(input("How many participants will register? "))
    except ValueError:
        return 0

    if num_participants <= 0:
        print("Invalid number of participants.")
        return 0

    return num_participants

def collect_participants(num_participants):
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

def track_diversity_report(participants):
    unique_tracks = set(p["track"] for p in participants)

    if unique_tracks:
        print("\nTracks offered in this event:")
        print(", ".join(sorted(unique_tracks)))
        if len(unique_tracks) < 2:
            print("Not enough variety in tracks.")
    else:
        pass

    return unique_tracks

def duplicate_name_detection(participants):
    names_seen = set()
    duplicate_names = set()

    for p in participants:
        name = p["name"]
        if name in names_seen:
            duplicate_names.add(name)
        names_seen.add(name)

    print()
    if duplicate_names:
        for name in sorted(duplicate_names):
            print(f"Duplicate name found: {name}")
    else:
        print("No duplicate names.")

def track_summary_report(participants):
    track_counts = {}

    for p in participants:
        track = p["track"]
        track_counts[track] = track_counts.get(track, 0) + 1

    print("\nParticipants per track:")
    for track, count in sorted(track_counts.items()):
        print(f"{track}: {count}")

def main():
    num_participants = setup_registration()

    if num_participants > 0:
        participants = collect_participants(num_participants)
        track_diversity_report(participants)
        duplicate_name_detection(participants)
        track_summary_report(participants)

if __name__ == "__main__":
    main()