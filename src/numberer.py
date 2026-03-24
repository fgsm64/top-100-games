import os

def load_games(filename):
    """Load games from a text file into a list."""
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def save_games(filename, games):
    """Save the list of games to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(games))

def number_games(games):
    """Number the games in the list incrementally."""
    new_games = []
    for i, game in enumerate(games):
        new_games.append(str(i+1) + ". " + game)
    return new_games

def append_backloggd(filename):
    """Append a link to Backloggd at the end of the file."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write("\n\nList of what games I've played on [Backloggd](https://backloggd.com/u/fgsm/games/)\n")


def main():
    """Main function to load, number, and save games."""
    input_file = "src/top_100_games.txt"
    output_file = "README.md"

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        return

    games = load_games(input_file)
    numbered_games = number_games(games)
    save_games(output_file, numbered_games)
    append_backloggd(output_file)

if __name__ == "__main__":
    main()
