from collections import Counter
from itertools import compress
from typing import List

with open("2021/day_3.txt") as f:
    data = f.read().splitlines()


def common(stream: List[str]) -> str:
    count = Counter(stream).most_common()
    if len(count) == 1 or count[0][1] != count[1][1]:
        return count[0][0]
    else:
        return 1


def validate(streams: List[List[str]], valid: List[bool], f) -> None:
    for stream in streams:
        stream_valid = f(stream, valid)
        for j, row in enumerate(stream):
            if valid.count(True) == 1:
                break
            if row != stream_valid:
                valid[j] = False


def puzzle_1(streams: List[List[str]]) -> int:
    gamma = int("".join(common(s) for s in streams), base=2)
    epsilon = ~gamma & int("1" * len(streams), base=2)
    return gamma * epsilon


def puzzle_2(streams: List[List[str]], data: List[str]) -> int:
    valid = [
        [True for _ in range(len(streams[0]))],  # Oxygen
        [True for _ in range(len(streams[0]))],  # CO2
    ]
    validate(streams, valid[0], lambda a, b: common(list(compress(a, b))))  # Oxygen
    validate(
        streams, valid[1], lambda a, b: str(1 - int(common(list(compress(a, b)))))
    )  # CO2

    return int(data[valid[0].index(True)], base=2) * int(
        data[valid[1].index(True)], base=2
    )


if __name__ == "__main__":
    streams = [[row[i] for row in data] for i, _ in enumerate(data[0])]
    print(f"Puzzle 1: {puzzle_1(streams)}")
    print(f"Puzzle 2: {puzzle_2(streams, data)}")
