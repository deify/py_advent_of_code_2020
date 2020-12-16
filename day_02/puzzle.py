from typing import Any, Dict
import re


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
        self.parse_data = []
        for line in self.puzzle_data.split("\n"):
            m = re.match(
                r"(?P<min>\d*)-(?P<max>\d*)\s(?P<char>\w):\s(?P<password>.*)", line
            )
            if m:

                d: Dict[str, Any] = m.groupdict()
                for k in ["min", "max"]:
                    d[k] = int(d[k])
                self.parse_data.append(d)

    def solve_part1(self, **kwargs):
        rule_fullfilled = [
            rule["min"] <= rule["password"].count(rule["char"]) <= rule["max"]
            for rule in self.parse_data
        ]
        self.part1_result = sum(rule_fullfilled)

    def solve_part2(self, **kwargs):
        rule_fullfilled = [
            (rule["password"][rule["min"] - 1] == rule["char"])
            ^ (rule["password"][rule["max"] - 1] == rule["char"])
            for rule in self.parse_data
        ]

        self.part2_result = sum(rule_fullfilled)
