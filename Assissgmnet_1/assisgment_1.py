"""
Name: Asmita Sharma
Date started: 20/12/2023
GitHub URL:https://github.com/JCUS-CP1404/cp1404-song-list-assignment-1-asharma151515/blob/master/assignment1.py

This program is a simple song list that allows a user to track songs that they wish to learn and
songs they have completed learning.
"""

FILENAME = "songs.csv"
LEARNED = "l"
UNLEARNED = "u"
MENU = """Menu:
D - Display songs
A - Add new songs
C - Complete a song
Q - Quit"""


def main():
    """This function manages the programs main menu and user interactions.
    Users can choose to display songs, add new songs, complete a song, or quit the program."""
    songs = read_file()
    print("Song List 1.0 - by Asmita Sharma")
    print(f"{len(songs)} songs loaded")
    print(MENU)

    while True:
        choice = input(">>> ").upper()

        if choice == "D":
            display_songs(songs)
        elif choice == "A":
            print("Enter details for a new song.")
            add_new_song(songs)
        elif choice == "C":
            print("Enter the number of a song to mark as learned.")
            complete_song(songs)
        elif choice == "d":  # Handle lowercase 'd' differently
            print("Enter the number of a song to mark as learned.")
            complete_song(songs)
        elif choice == "Q":
            write_file(songs)
            print(f"{len(songs)} songs saved to {FILENAME}")
            print("Make some music!")
            break
        else:
            print("Invalid menu choice")

        print(MENU)



def read_file():
    """Read song data from a CSV file and return a list of song records."""
    with open(FILENAME, "r") as in_file:
        songs = []
        for line in in_file:
            parts = line.strip().split(",")
            songs.append(parts)
        return songs


def write_file(songs):
    """Write song data to a CSV file."""
    with open(FILENAME, "w") as out_file:
        for song in songs:
            out_file.write(",".join(map(str, song)) + "\n")


def add_new_song(songs):
    """Add a new song to the list of songs."""
    title = get_valid_input("Title:  ")
    artist = get_valid_input("Artist: ")
    year = get_valid_number("Year: ")
    songs.append([title.title(), artist.title(), year, UNLEARNED])
    print(f"{title.title()} by {artist.title()} ({year}) added to song list.")


def display_songs(songs):
    """Display the list of songs with their details."""
    learned_count = sum(1 for song in songs if song[3] == LEARNED)
    unlearned_count = sum(1 for song in songs if song[3] == UNLEARNED)

    # Convert year to integer for proper sorting
    for song in songs:
        try:
            song[2] = int(song[2])
        except ValueError:
            # Handle if the year is not a valid integer
            pass

    sorted_songs = sorted(songs, key=lambda song: (song[2], song[0]))
    max_title_length = max(len(song[0]) for song in songs)
    max_artist_length = max(len(song[1]) for song in songs)
    for i, song in enumerate(sorted_songs, start=1):
        learned_condition = "*" if song[3] == UNLEARNED else ""
        print(f"{i}. {learned_condition:2} {song[0]:{max_title_length}} - {song[1]:{max_artist_length}} ({song[2]})")

    print(f"{learned_count} songs learned, {unlearned_count} songs still to learn.")


def complete_song(songs):
    """Mark a song as learned in the list of songs."""
    is_song_completed = False
    while not is_song_completed:
        song_number = get_valid_number(">>> ")
        if 1 <= song_number <= len(songs):
            if songs[song_number - 1][3] == LEARNED:
                print(f"You have already learned {songs[song_number - 1][0]}")
            else:
                print(f"{songs[song_number - 1][0]} by {songs[song_number - 1][1]} learned")
                songs[song_number - 1][3] = LEARNED
                # Update learned and unlearned counts
                unlearned_count = sum(1 for song in songs if song[3] == UNLEARNED)
                learned_count = len(songs) - unlearned_count
                print(f"{learned_count} songs learned, {unlearned_count} songs still to learn.")
            is_song_completed = True
        else:
            print("Invalid song number")


def get_valid_number(prompt):
    """Get a valid integer input from the user."""
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Number must be > 0.")
        except ValueError:
            print("Invalid input; enter a valid number.")


def get_valid_input(prompt):
    """Get a valid non-empty string input from the user."""
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input.strip()
        else:
            print("Input can not be blank.")


if __name__ == '__main__':
    main()
