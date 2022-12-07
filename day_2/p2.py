# (user_choice - pc_choice) % 3 = outcome
# 0 (tie)
# 1 (user wins)
# 2 (computer wins)

LOSS = 2
DRAW = 0
WIN = 1


replacements = {"A": 1, "B": 2, "C": 3}
game_outcomes = {"X": LOSS, "Y": DRAW, "Z": WIN}
score_bonus = {LOSS: 0, DRAW: 3, WIN: 6}


def calculate_player_score(enemy_choice: int, game_result: int):
    user_choice = (game_result + enemy_choice) % 3
    if user_choice == 0:
        user_choice = 3
    return user_choice + score_bonus[game_result]


with open('./input.txt', 'r') as f:
    SCORE = 0
    myline = f.readline()
    while myline:
        SCORE += calculate_player_score(
            replacements[myline[0]], game_outcomes[myline[2]])
        myline = f.readline()
    f.close()
    print(SCORE)
