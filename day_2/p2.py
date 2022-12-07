# (user_choice - pc_choice) % 3 = outcome
# 0 (tie)
# 1 (user wins)
# 2 (computer wins)

# Outcomes:
# X = loss
# Y = draw
# Z = win

# Score bonuses
# Lose: 0
# Tie: 3
# Win: 6

replacements = {"A": 1, "B": 2, "C": 3}
game_outcomes = {"X": 2, "Y": 0, "Z": 1}
score_bonus = {2: 0, 0: 3, 1: 6}


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
