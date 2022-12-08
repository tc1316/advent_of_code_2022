with open("./input.txt") as f:
    line = f.readline().strip()

    markers = []
    last_duplicate = 0
    current = 0
    while len(markers) != 14:

        if line[current] in markers:
            last_duplicate += 1
            markers = [line[last_duplicate]]
            current = last_duplicate
        else:
            markers.append(line[current])

        current += 1
    print(current)
