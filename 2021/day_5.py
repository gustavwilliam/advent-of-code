import re
from dataclasses import dataclass
from itertools import product, chain
from typing import List, NamedTuple, Literal

Point = NamedTuple("Point", [("x", int), ("y", int)])
Direction = Literal["horizontal", "vertical"]

with open("2021/day_5.txt") as f:
    data = f.read().splitlines()


@dataclass
class Line:
    start: Point
    end: Point

    def __post_init__(self):
        self.max = Point(max(self.start.x, self.end.x), max(self.start.y, self.end.y))
        self.min = Point(min(self.start.x, self.end.x), min(self.start.y, self.end.y))

        if self.start.x == self.end.x:
            self.direction = "horizontal"
        elif self.start.y == self.end.y:
            self.direction = "vertical"
        else:
            self.direction = int(
                (self.end.y - self.start.y) / (self.end.x - self.start.x)
            )

    def collides(self, point: Point) -> bool:
        if isinstance(direction := self.direction, int):
            return False
        if (
            direction == "vertical"
            and self.start.y == point.y
            and self.max.x >= point.x
            and self.min.x <= point.x
        ) or (
            direction == "horizontal"
            and self.start.x == point.x
            and self.max.y >= point.y
            and self.min.y <= point.y
        ):
            return True
        return False


@dataclass
class Board:
    lines: List[Line]

    def __post_init__(self):
        self.max = Point(
            max(line.max.x for line in self.lines),
            max(line.max.y for line in self.lines),
        )

    def hits(self) -> int:
        total_hits = 0
        for x, y in product(range(self.max.x + 1), range(self.max.y + 1)):
            point = Point(x, y)
            if sum([line.collides(point) for line in self.lines]) > 1:
                total_hits += 1

        return total_hits

    def prune_tilted(self):
        self.lines = [
            line for line in self.lines if not isinstance(line.direction, int)
        ]


def parse_raw(data: List[str]) -> List[Line]:
    lines = [[int(num) for num in re.findall(r"\d+", line)] for line in data]
    return [Line(Point(line[0], line[1]), Point(line[2], line[3])) for line in lines]


def puzzle_1(board: Board) -> int:
    board.prune_tilted()
    return board.hits()


if __name__ == "__main__":
    board = Board(parse_raw(data))
    print(puzzle_1(board))
