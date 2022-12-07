# (user_choice - pc_choice) % 3
# 0 (tie)
# 1 (user wins)
# 2 (computer wins)

replacements = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def calculate_bonus_score(number: int):
    match number:
        case 0:
            return 3
        case 1:
            return 6
        case 2:
            return 0


def calculate_player_score(enemy_choice: int, player_choice: int):
    return calculate_bonus_score(
        ((player_choice - enemy_choice) %
         3)) + player_choice


with open('./input.txt', 'r') as f:
    SCORE = 0
    myline = f.readline()
    while myline:
        SCORE += calculate_player_score(
            replacements[myline[0]], replacements[myline[2]])
        myline = f.readline()
    f.close()
    print(SCORE)
