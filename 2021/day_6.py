from itertools import chain
from typing import List


with open("2021/day_6.txt") as f:
    data = [int(fish) for fish in f.read().split(",")]


def increment_age(timer: int) -> List[int]:
    return [6, 8] if timer == 0 else [timer - 1]


def puzzle_1(data: List[int], days: int) -> int:
    for _ in range(days):
        data = list(chain(*[increment_age(fish) for fish in data]))
    return len(data)


def puzzle_2(data: List[int]) -> int:
    ...


if __name__ == "__main__":
    print(f"Puzzle 1: {puzzle_1(data, 80)}")
    # print(f"Puzzle 2: {puzzle_2(data)}")
