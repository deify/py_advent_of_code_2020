from typing import Any
import itertools
import numpy as np


class puzzle:
    puzzle_data: str = ""
    parse_data: Any = None
    part1_result: Any = None
    part2_result: Any = None

    def __init__(self, data_path):
        super().__init__()
        with open(data_path, "r") as file:
            self.puzzle_data = file.read()

    def parse(self, **kwargs):
        self.parse_data = list(map(int, self.puzzle_data.split("\n")))

    def solve_part1(self, **kwargs):
        combinations = list(itertools.combinations(self.parse_data, 2))

        self.part1_result = self.find_prod(combinations)

    def solve_part2(self, **kwargs):
        combinations = list(itertools.combinations(self.parse_data, 3))
        self.part2_result = self.find_prod(combinations)

    def find_prod(self, combinations):
        for element in combinations:
            if sum(element) == 2020:
                return np.prod(element)
