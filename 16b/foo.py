north = (-1, 0)
south = (1, 0)
east = (0, 1)
west = (0, -1)


def progress_beam(beam):
    bp, bv = beam
    next_position = (bp[0] + bv[0], bp[1] + bv[1])
    next_char = position.get(next_position, {}).get("char", False)

    # grid boundary
    if not next_char:
        return []
    # been here from this direction already
    elif bv in position.get(next_position).get("seen_heading"):
        return []
    # else mark next position seen
    else:
        position[next_position]["seen_heading"].append(bv)

    # continue
    if (
        next_char == "."
        or (bv in [north, south] and next_char == "|")
        or (bv in [east, west] and next_char == "-")
    ):
        return [(next_position, bv)]
    # split
    if bv in [north, south] and next_char == "-":
        return [(next_position, east), (next_position, west)]
    if bv in [east, west] and next_char == "|":
        return [(next_position, north), (next_position, south)]
    # turn
    if (bv == north and next_char == "/") or (bv == south and next_char == "\\"):
        return [(next_position, east)]
    if (bv == north and next_char == "\\") or (bv == south and next_char == "/"):
        return [(next_position, west)]
    if (bv == east and next_char == "/") or (bv == west and next_char == "\\"):
        return [(next_position, north)]
    if (bv == east and next_char == "\\") or (bv == west and next_char == "/"):
        return [(next_position, south)]


def main_part_2(data):
    global position
    max_y = 0
    max_x = 0
    position = dict()
    for y, line in enumerate(data.strip().split("\n")):
        if y > max_y:
            max_y = y
        for x, char in enumerate(line):
            if x > max_x:
                max_x = x
            position[y, x] = {"char": char, "seen_heading": []}

    start_beams = [((y, 0), east) for y in range(0, max_y + 1)]
    start_beams.extend([((y, max_x), west) for y in range(0, max_y + 1)])
    start_beams.extend([((0, x), south) for x in range(0, max_x + 1)])
    start_beams.extend([((max_y, x), north) for x in range(0, max_x + 1)])

    results = []

    for start_beam in start_beams:
        beams = [start_beam]
        go = True
        while go:
            new_beams = []
            for beam in beams:
                new_beams.extend(progress_beam(beam))
            if len(new_beams) == 0:
                go = False
            else:
                beams = new_beams

        results.append(
            len([a for a in position.values() if a.get("seen_heading") != []])
        )

        for p in position.keys():
            position[p]["seen_heading"] = []

    return max(results)


def main_part_1(data):
    global position
    position = dict()
    for y, line in enumerate(data.strip().split("\n")):
        for x, char in enumerate(line):
            position[y, x] = {"char": char, "seen_heading": []}

    beams = [((0, -1), east)]
    go = True
    while go:
        new_beams = []
        for beam in beams:
            new_beams.extend(progress_beam(beam))
        if len(new_beams) == 0:
            go = False
        else:
            beams = new_beams

    return len([a for a in position.values() if a.get("seen_heading") != []])
