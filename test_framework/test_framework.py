import inspect
import os
import yaml
from typing import Dict, Any
import nose  # type: ignore
import nose.tools as nt  # type: ignore


class ConfigDict:
    parse_args: Dict[str, Any] = {}
    parse_result: Any = None

    part1_args: Dict[str, Any] = {}
    part1_result: Any = None

    part2_args: Dict[str, Any] = {}
    part2_result: Any = None

    def __init__(self, config_dict):
        super().__init__()
        if config_dict == None:
            config_dict = {}
        # using "or" rather than dict.get(key,default) is done to prevent None entries
        self.parse_args = config_dict.get("parse_args") or {}
        self.parse_result = config_dict.get("parse_result") or ""
        self.part1_args = config_dict.get("part1_args") or {}
        self.part1_result = config_dict.get("part1_result") or ""
        self.part2_args = config_dict.get("part2_args") or {}
        self.part2_result = config_dict.get("part2_result") or ""


class BasePuzzleTest:
    test_config: ConfigDict

    def __init__(self, puzzle, config_path):
        super().__init__()
        self.test_puzzle = puzzle
        with open(config_path, "r") as file:
            self.test_config = ConfigDict(yaml.load(file, Loader=yaml.FullLoader))

    def setup(self):
        pass

    def teardown(self):
        pass

    # this is where the actual test section starts
    def test_check_loaded_puzzle_data(self):
        # assertion
        nt.assert_not_equal(self.test_puzzle.puzzle_data, "")

    def test_puzzle_parse(self):
        if self.test_config.parse_args.get("skip", False):
            raise nose.SkipTest("Skipped parse test because configured by user")

        self.test_puzzle.parse(**self.test_config.parse_args)
        # assertion
        nt.assert_equal(self.test_puzzle.parse_data, self.test_config.parse_result)

    def test_puzzle_part1(self):
        if self.test_config.part1_args.get("skip", False):
            raise nose.SkipTest("Skipped part1 test because configured by user")
        self.test_puzzle.parse(**self.test_config.parse_args)
        self.test_puzzle.solve_part1(**self.test_config.part1_args)

        # assertion
        nt.assert_equal(self.test_puzzle.part1_result, self.test_config.part1_result)

    def test_puzzle_part2(self):
        if self.test_config.part2_args.get("skip", False):
            raise nose.SkipTest("Skipped part2 test because configured by user")
        self.test_puzzle.parse(**self.test_config.parse_args)
        self.test_puzzle.solve_part2(**self.test_config.part2_args)

        # assertion
        nt.assert_equal(self.test_puzzle.part2_result, self.test_config.part2_result)

