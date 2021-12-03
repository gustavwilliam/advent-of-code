from typing import List


with open("2021/day_3.txt") as f:
    data = f.read().splitlines()


def gamma(data: List[str]) -> int:
    vals = [0] * len(data[0])
    for row in data:
        for i, val in enumerate(row):
            vals[i] += 1 if val == "1" else -1

    val = "".join(str(int(i >= 0)) for i in vals)
    return int(val, base=2)


def epsilon(data: List[str]) -> int:
    return ~gamma(data) & int("1" * len(data[0]), base=2)


def puzzle_1(data: List[str]) -> int:
    return gamma(data) * epsilon(data)


if __name__ == "__main__":
    print(f"Puzzle 1: {puzzle_1(data)}")
