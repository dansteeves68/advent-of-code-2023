#!/usr/bin/env python3

def game_parser(line):
    game, sample_str = line.split(":")
    
    game_id = int(game.split(" ")[1])

    samples = []
    for sample in sample_str.split(";"):
        sample = [a.strip() for a in sample.split(",")]
        s_ = {}
        for s in sample:
            count, color = s.split(" ")
            s_[color] = int(count)
        samples.append(s_)

    return {"game_id": game_id, "samples": samples}

def game_tester(bag, samples):
    result = True
    for sample in samples:
        for color in sample.keys():
            if sample.get(color) > bag.get(color):
                result = False
    return result

def game_minimizer(samples):
    result = {"red": 0, "green": 0, "blue": 0}
    for sample in samples:
        for color in sample.keys():
            if sample.get(color) > result.get(color):
                result[color] = sample.get(color)
    return result

def power(bag):
    return bag.get("red") * bag.get("green") * bag.get("blue")


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        contents = f.read()
    games = contents.split("\n")
    games = [game_parser(a) for a in games]
    results = []
    for game in games:
        if game_tester(bag={"red": 12, "green": 13, "blue": 14}, samples=game.get("samples")):
            results.append(game.get("game_id"))
    print("Game Tester Result", sum(results))

    results = []
    for game in games:
        results.append(game_minimizer(samples=game.get("samples")))
    results = sum([power(bag=a) for a in results])
    print("Game Minimizer Results", results)
