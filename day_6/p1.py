with open("./input.txt") as f:
    line = f.readline()

    markers = set()
    c = 1
    for char in line:

        if char not in markers:
            markers.add(char)
            if len(markers) == 4:
                break
        elif char in markers:
            markers = set()
        c += 1

    print(c)
