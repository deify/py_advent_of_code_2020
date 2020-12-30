from typing import Any, Dict


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
        passports = []
        d: Dict[str, Any] = {}

        for line in self.puzzle_data.split("\n"):
            if not line:
                if d:
                    d = self.cast_passport_dict(d)
                    passports.append(d)
                d = {}
            else:
                for entry in line.split(" "):
                    key, value = entry.split(":")
                    d[key] = value

        d = self.cast_passport_dict(d)
        passports.append(d)
        self.parse_data = passports

    def cast_passport_dict(self, d: Dict[str, Any]) -> Dict[str, Any]:
        for key in ["eyr", "byr", "iyr", "cid"]:
            if key in d:
                d[key] = int(d[key])
        return d

    def solve_part1(self, **kwargs):
        valid_passports = [
            PassPortValidator(passport).all_required_keys_exist()
            for passport in self.parse_data
        ]

        self.part1_result = sum(valid_passports)

    def solve_part2(self, **kwargs):
        if "test" in kwargs:
            self.puzzle_data = kwargs["test"]["invalid_passports"]
            self.parse()
            invalid = not all(
                [PassPortValidator(passport).is_valid() for passport in self.parse_data]
            )
            self.puzzle_data = kwargs["test"]["valid_passports"]
            self.parse()
            valid = all(
                [PassPortValidator(passport).is_valid() for passport in self.parse_data]
            )
            print(invalid, valid)
            self.part2_result = valid + invalid
        else:
            valid_passports = [
                PassPortValidator(passport).is_valid() for passport in self.parse_data
            ]
            self.part2_result = sum(valid_passports)


import regex as re


class PassPortValidator:
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    def __init__(self, pass_dict):
        self.pass_dict = pass_dict

        self.all_rules = [
            self.byr_valid,
            self.iyr_valid,
            self.eyr_valid,
            self.hgt_valid,
            self.hcl_valid,
            self.ecl_valid,
            self.pid_valid,
        ]

    def all_required_keys_exist(self):
        return all(key in self.pass_dict for key in PassPortValidator.required_keys)

    def is_valid(self):
        if not self.all_required_keys_exist():
            return False
        for rule in self.all_rules:
            if not rule():
                return False

        return True

    def byr_valid(self):
        return 1920 <= self.pass_dict["byr"] <= 2002

    def iyr_valid(self):
        return 2010 <= self.pass_dict["iyr"] <= 2020

    def eyr_valid(self):
        return 2020 <= self.pass_dict["eyr"] <= 2030

    def hgt_valid(self):
        valid = False
        m = re.match(r"^(?P<value>\d*)(?P<unit>(in|cm))$", self.pass_dict["hgt"])
        if m:
            if m.group("unit") == "in":
                valid = 59 <= int(m.group("value")) <= 76
            elif m.group("unit") == "cm":
                valid = 150 <= int(m.group("value")) <= 193

        return valid

    def hcl_valid(self):
        m = re.match(r"^#[0-9a-f]{6}$", self.pass_dict["hcl"])
        return m is not None

    def ecl_valid(self):
        valid_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        return self.pass_dict["ecl"] in valid_colors

    def pid_valid(self):
        m = re.match(r"^\d{9}$", self.pass_dict["pid"])
        return m is not None
