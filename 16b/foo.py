north = (-1, 0)
south = (1, 0)
east = (0, 1)
west = (0, -1)


def progress_beam(beam):
    bp, bv = beam
    next_position = (bp[0] + bv[0], bp[1] + bv[1])
    next_char = position.get(next_position, {}).get("char", False)
    print("Next position & char: ", next_position, next_char)

    # grid boundary
    if not next_char:
        return []
    # been here from this direction already
    elif bv in position.get(next_position).get("seen_heading"):
        return []
    # else mark next position seen
    else:
        print(position.get(next_position).get("seen_heading"))
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


def main_part_1(data):
    global position
    position = dict()
    for y, line in enumerate(data.strip().split("\n")):
        for x, char in enumerate(line):
            print(y, x, char)
            position[y, x] = {"char": char, "seen_heading": []}

    print(position)
    beams = [((0, -1), east)]
    go = True
    while go:
        print("Starting loop with beams: ", beams)
        new_beams = []
        for beam in beams:
            new_beams.extend(progress_beam(beam))
            print("Beam ", beam, "resulted in new beams", new_beams)
        if len(new_beams) == 0:
            go = False
        else:
            beams = new_beams

    return len([a for a in position.values() if a.get("seen_heading") != []])
