#!/usr/bin/env python3


def hash(input: str) -> int:
    value = 0
    for char in input:
        value += ord(char)
        value = value * 17
        value = value % 256
    return value


def init(data: str) -> int:
    total = 0
    for step in data.split(","):
        total += hash(input=step)
    return total


class Boxes:
    def __init__(self):
        self.boxes = [[] for a in range(0, 256)]

    def process(self, instruction):
        if instruction[-1] == "-":
            focal_length = None
            label = instruction[:-1]
            box = hash(label)
            self.boxes[box] = [a for a in self.boxes[box] if a[0] != label]
        else:
            focal_length = instruction[-1]
            label = instruction[:-2]
            box = hash(label)
            if label in [a[0] for a in self.boxes[box]]:
                index = [a[0] for a in self.boxes[box]].index(label)
                self.boxes[box][index] = (label, focal_length)
            else:
                self.boxes[box].append((label, focal_length))
        # print(instruction, box, label, focal_length, self.boxes[:4])

    def score(self):
        score = 0
        for i, box in enumerate(self.boxes):
            for j, lens in enumerate(box):
                score += (i + 1) * (j + 1) * int(lens[1])
                # print(i, j, lens[1], score)
        return score


def main(data):
    box = Boxes()
    for instruction in data.split(","):
        box.process(instruction=instruction)
    print(box.boxes)
