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


def puzzle_1(streams: List[List[str]]) -> int:
    gamma = int("".join(common(s) for s in streams), base=2)
    epsilon = ~gamma & int("1" * len(streams), base=2)
    return gamma * epsilon


def puzzle_2(streams: List[List[str]], data: List[str]) -> int:
    valid = [[True for _ in range(len(streams[0]))] for _ in range(2)]

    for stream in streams:
        o2 = common(list(compress(stream, valid[0])))
        for j, row in enumerate(stream):
            if valid[0].count(True) == 1:
                break
            if row != o2:
                valid[0][j] = False

    for stream in streams:
        co2 = str(1 - int(common(list(compress(stream, valid[1])))))
        for j, row in enumerate(stream):
            if valid[1].count(True) == 1:
                break
            if row != co2:
                valid[1][j] = False

    return int(data[valid[0].index(True)], base=2) * int(
        data[valid[1].index(True)], base=2
    )


if __name__ == "__main__":
    streams = [[row[i] for row in data] for i, _ in enumerate(data[0])]
    print(f"Puzzle 1: {puzzle_1(streams)}")
    print(f"Puzzle 2: {puzzle_2(streams, data)}")
