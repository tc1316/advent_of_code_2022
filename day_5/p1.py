CLEANED_INPUT = []
with open('./input_state.txt') as f:
    line = f.readline().strip()
    while line:
        CLEANED_INPUT.append(list(line))
        line = f.readline().strip()


def parse_moves(moves: str):
    split_moves = (moves.split(' '))
    return (int(split_moves[1]), int(split_moves[3]), int(split_moves[5]))


def move_crates(stacks: list[list[str]], moves: tuple[int, int, int]):
    quantity_to_move, move_from, move_to = moves[0], moves[1]-1, moves[2]-1

    for _ in range(quantity_to_move):
        stacks[move_to].append(stacks[move_from].pop())


with open('./input_instructions.txt') as f:
    line = f.readline()
    input_data = CLEANED_INPUT
    while line:
        move_crates(input_data, parse_moves(line))
        line = f.readline()

    ANSWER = ''
    for stack in input_data:
        ANSWER += stack[-1]
    print(ANSWER)
