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
        self.parse_data = [list(line) for line in self.puzzle_data.split("\n")]

    def solve_part1(self, **kwargs):

        self.part1_result = self.sled_down(
            kwargs["slope"][0]["down"], kwargs["slope"][0]["right"]
        )

    def solve_part2(self, **kwargs):
        result = 1
        for slope in kwargs["slope"]:
            result *= self.sled_down(slope["down"], slope["right"])
        self.part2_result = result

    def sled_down(self, slope_down, slope_right):
        dim_down = len(self.parse_data)
        dim_right = len(self.parse_data[0])
        pos_down = 0
        pos_right = 0
        tree_count = 0
        while pos_down < dim_down:
            if pos_right >= dim_right:
                pos_right = pos_right - dim_right

            if self.parse_data[pos_down][pos_right] == "#":
                tree_count += 1

            pos_right += slope_right
            pos_down += slope_down

        return tree_count
