import re
import numpy as np
from typing import Generator, List, Tuple

Data = List[Tuple[Tuple[int, int], Tuple[int, int]]]

with open("2021/day_5.txt") as f:
    data = f.read().splitlines()


def parse_raw(
    data: List[str],
) -> Generator[Tuple[Tuple[int, int], Tuple[int, int]], None, None]:
    for line in data:
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
        yield (x1, y1), (x2, y2)


def intersections(
    line: Tuple[Tuple[int, int], Tuple[int, int]]
) -> List[Tuple[int, int]]:
    (x1, y1), (x2, y2) = line
    if x1 == x2:
        return [(x1, y) for y in (range(y1, y2 + 1) if y2 >= y1 else range(y2, y1 + 1))]
    if y1 == y2:
        return [(x, y1) for x in (range(x1, x2 + 1) if x2 >= x1 else range(x2, x1 + 1))]

    tilt = (y2 - y1) // (x2 - x1)  # 1 or -1
    if x2 < x1:
        (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
    return [(x1 + x, y1 + x * tilt) for x in range(0, x2 - x1 + 1)]


def hits(data: Data) -> int:
    grid = np.zeros((1000, 1000), dtype=int)  # type: ignore
    for line in data:
        for x, y in intersections(line):
            grid[y][x] += 1  # type: ignore

    return (grid > 1).sum()  # type: ignore


def puzzle_1(data: Data) -> int:
    return hits(
        ((x1, y1), (x2, y2)) for (x1, y1), (x2, y2) in data if x1 == x2 or y1 == y2
    )


def puzzle_2(data: Data) -> int:
    return hits(data)


if __name__ == "__main__":
    data = list(parse_raw(data))
    print(f"Puzzle 1: {puzzle_1(data)}")
    print(f"Puzzle 2: {puzzle_2(data)}")
