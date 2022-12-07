def convert_uppercase(char: str):
    return ord(char)-38


def convert_lowercase(char: str):
    return ord(char)-96


def get_priority_value(char: str):
    if char.isupper():
        return convert_uppercase(char)
    return convert_lowercase(char)


with open('./input.txt') as f:
    VALUE = 0
    line = f.readline().strip()
    while line:
        first_set = set()
        second_set = set()

        p1 = 0
        p2 = len(line)-1
        while p1 < p2:
            first_set.add(line[p1])
            second_set.add(line[p2])
            p1 += 1
            p2 -= 1
        common_char = first_set.intersection(second_set)
        if len(common_char):
            VALUE += get_priority_value(common_char.pop())
        line = f.readline().strip()
    print(VALUE)
