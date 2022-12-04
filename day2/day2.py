WIN = 6
DRAW = 3
LOSS = 0

WEAPON = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"file {filename} does not exist")
        return None

def calculate_score(rps_games):
    my_score = 0
    for game in rps_games:
        opponent_game = game[0]
        me_game = game[2]
        if WEAPON[opponent_game] == "rock" and WEAPON[me_game] == "paper":
            my_score += WIN + SCORES[me_game]
        elif WEAPON[opponent_game] == "rock" and WEAPON[me_game] == "scissors":
            my_score += LOSS + SCORES[me_game]
        elif WEAPON[opponent_game] == "paper" and WEAPON[me_game] == "rock":
            my_score += LOSS + SCORES[me_game]
        elif WEAPON[opponent_game] == "paper" and WEAPON[me_game] == "scissors":
            my_score += WIN + SCORES[me_game]
        elif WEAPON[opponent_game] == "scissors" and WEAPON[me_game] == "paper":
            my_score += LOSS + SCORES[me_game]
        elif WEAPON[opponent_game] == "scissors" and WEAPON[me_game] == "rock":
            my_score += WIN + SCORES[me_game]
        elif WEAPON[opponent_game] == WEAPON[me_game]:
            my_score += DRAW + SCORES[me_game]
    return my_score

def calculate_score_part_2(rps_games):
    round_ends_with = {
        "X": "lose",
        "Y": "draw",
        "Z": "win"
    }
    my_score = 0
    for game in rps_games:
        opponent_game = game[0]
        game_end = game[2]
        if WEAPON[opponent_game] == "rock" and round_ends_with[game_end] == "win":
            my_score += WIN + SCORES["Y"]
        elif WEAPON[opponent_game] == "paper" and round_ends_with[game_end] == "win":
            my_score += WIN + SCORES["Z"]
        elif WEAPON[opponent_game] == "scissors" and round_ends_with[game_end] == "win":
            my_score += WIN + SCORES["X"]
        elif WEAPON[opponent_game] == "rock" and round_ends_with[game_end] == "draw":
            my_score += DRAW + SCORES["X"]
        elif WEAPON[opponent_game] == "paper" and round_ends_with[game_end] == "draw":
            my_score += DRAW + SCORES["Y"]
        elif WEAPON[opponent_game] == "scissors" and round_ends_with[game_end] == "draw":
            my_score += DRAW + SCORES["Z"]
        elif WEAPON[opponent_game] == "rock" and round_ends_with[game_end] == "lose":
            my_score += LOSS + SCORES["Z"]
        elif WEAPON[opponent_game] == "paper" and round_ends_with[game_end] == "lose":
            my_score += LOSS + SCORES["X"]
        elif WEAPON[opponent_game] == "scissors" and round_ends_with[game_end] == "lose":
            my_score += LOSS + SCORES["Y"]
    return my_score
      


def main():
    """
    Opponent -> rock = A, paper = B, scissor = C
    You      -> rock = x, paper = y, scissor = z
    (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus the score for the outcome of the round 
    (0 if you lost, 3 if the round was a draw, and 6 if you won)
    """

    # Part 1
    lines = read_file("./day2/real.txt")
    my_score = calculate_score(lines)
    print(my_score)

    # Part 2
    my_score = calculate_score_part_2(lines)
    print(my_score)

main()