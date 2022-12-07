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
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    line3 = f.readline().strip()
    while line3:
        first_set = set(char for char in line1)
        second_set = set(char for char in line2)
        third_set = set(char for char in line3)

        common_char = first_set & second_set & third_set
        VALUE += get_priority_value(common_char.pop())
        line1 = f.readline().strip()
        line2 = f.readline().strip()
        line3 = f.readline().strip()
    print(VALUE)
