import numpy as np

with open("2021/day_7.txt") as f:
    data: np.ndarray = np.fromiter(f.read().split(","), dtype=int)


def mean(data: np.ndarray, f) -> int:
    median = int(np.median(data))
    lowest: int | None = None
    for guess in range(median - 10, median + 10):
        cost = sum(np.fromiter((f(guess, val) for val in data), dtype=int))
        if lowest is None:
            lowest = cost
        elif cost < lowest:
            lowest = cost

    return lowest or 0


def puzzle_1(data: np.ndarray) -> int:
    return mean(data, lambda guess, val: abs(guess - val))


def puzzle_2(data: np.ndarray) -> int:
    ...


if __name__ == "__main__":
    print(f"Puzzle 1: {puzzle_1(data)}")
    # print(f"Puzzle 2: {puzzle_2(data)}")
