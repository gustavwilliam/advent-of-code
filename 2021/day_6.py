from collections import Counter
from typing import List

with open("2021/day_6.txt") as f:
    data = [int(fish) for fish in f.read().split(",")]


def fish_count(data: List[int], days: int) -> int:
    fish = [0] * 9
    for i, val in Counter(data).items():
        fish[i] = val

    for _ in range(days):
        new = fish.pop(0)
        fish[6] += new
        fish.append(new)

    return sum(fish)


def puzzle_1(data: List[int]) -> int:
    return fish_count(data, 80)


def puzzle_2(data: List[int]) -> int:
    return fish_count(data, 256)


if __name__ == "__main__":
    print(f"Puzzle 1: {puzzle_1(data)}")
    print(f"Puzzle 2: {puzzle_2(data)}")
