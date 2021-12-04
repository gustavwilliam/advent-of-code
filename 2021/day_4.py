from dataclasses import dataclass
from itertools import compress
from typing import Generator, List, Tuple


with open("2021/day_4.txt") as f:
    data = f.read().split("\n\n")


@dataclass
class Board:
    rows: List[List[int]]

    def __post_init__(self):
        self.marked = [[False] * 5, [False] * 5, [False] * 5, [False] * 5, [False] * 5]
        self.bingo_value: int | None = None
        self.completed = False

    def new_value(self, value: int) -> None:
        for i, row in enumerate(self.rows):
            if value in row:
                self.marked[i][row.index(value)] = True

    def bingo(self) -> bool:
        cols = [list(col) for col in zip(*self.marked)]
        if any(all(row) for row in self.marked) or any(all(row) for row in cols):
            return True
        return False

    @property
    def sum_unmarked(self) -> int:
        compressed = compress(
            [i for sub in self.rows for i in sub],
            [not i for sub in self.marked for i in sub],
        )
        return sum(list(compressed))


def parse_raw(data: List[str]) -> Tuple[List[int], List[Board]]:
    inputs = [int(i) for i in data.pop(0).split(",")]
    board_data = []
    for item in data:
        board_data.append([[int(y) for y in x.split()] for x in item.split("\n")])

    return inputs, [Board(dat) for dat in board_data]


def get_all_bingo(data: Tuple[List[int], List[Board]]) -> Generator[Board, None, None]:
    for value in data[0]:
        for board in data[1]:
            if not board.completed:
                board.new_value(value)
                if board.bingo():
                    board.completed = True
                    board.bingo_value = value
                    yield board


def puzzle_1(data: Tuple[List[int], List[Board]]) -> int:
    board = next(get_all_bingo(data))
    return board.sum_unmarked * board.bingo_value


def puzzle_2(data: Tuple[List[int], List[Board]]) -> int:
    *_, board = get_all_bingo(data)
    return board.sum_unmarked * board.bingo_value


if __name__ == "__main__":
    data = parse_raw(data)
    print(f"Puzzle 1: {puzzle_1(data)}")
    print(f"Puzzle 2: {puzzle_2(data)}")
