import math
from typing import Dict, List, Union


with open("2021/day_2.txt") as f:
    data = f.read().splitlines()

modifiers = {
    "up": ["depth", -1],
    "down": ["depth", 1],
    "forward": ["horizontal", 1],
}


def parse_raw(data: List[str]) -> List[List[str]]:
    data = [i.split() for i in data]
    return [[i[0], int(i[1])] for i in data]


def puzzle_1(data: List[List[str]], modifiers: Dict[str, List[Union[str, int]]]) -> int:
    position = {"depth": 0, "horizontal": 0}

    for i in data:
        action, coefficient = i
        position[modifiers[action][0]] += coefficient * modifiers[action][1]

    return math.prod(position.values())


def puzzle_2(data: List[List[str]], modifiers: Dict[str, List[Union[str, int]]]) -> int:
    position = {"depth": 0, "horizontal": 0, "aim": 0}

    for i in data:
        action, coefficient = i
        if action == "forward":
            position["depth"] += coefficient * position["aim"]
            position["horizontal"] += coefficient
        else:
            position["aim"] += coefficient * modifiers[action][1]

    return position["depth"] * position["horizontal"]


if __name__ == "__main__":
    parsed = parse_raw(data)
    print(
        f"Puzzle 1: {puzzle_1(parsed, modifiers)}\n"
        f"Puzzle 2: {puzzle_2(parsed, modifiers)}"
    )
