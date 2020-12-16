from typing import Any


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
        self.parse_data = None

    def solve_part1(self, **kwargs):
        self.part1_result = None

    def solve_part2(self, **kwargs):
        self.part2_result = None
