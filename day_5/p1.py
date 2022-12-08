import re

CLEANED_INPUT = []
with open('./input_state.txt') as f:
    line = f.readline().strip()
    while line:
        CLEANED_INPUT.append(list(line))
        line = f.readline().strip()

# move 6 from 9 to 3


def parse_moves(moves: str):

    split_moves = (moves.split(' '))
    return (int(split_moves[1]), int(split_moves[3]), int(split_moves[5]))


def move_crates(input: list[list[str]], moves: tuple[int, int, int]):
    quantity_to_move, move_from, move_to = moves[0], moves[1]-1, moves[2]-1

    # print(input)
    for _ in range(quantity_to_move):
        if len(input[move_from]) != 0:
            input[move_to].append(input[move_from].pop())


with open('./input_instructions.txt') as f:
    line = f.readline()
    input = CLEANED_INPUT
    while line:
        move_crates(input, parse_moves(line))
        line = f.readline()

    ANSWER = ''
    for stack in input:
        ANSWER += stack[-1]
    print(ANSWER)
