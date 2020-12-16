from .puzzle import puzzle
from test_framework.test_framework import BasePuzzleTest
import inspect
import os


class TestPuzzle(BasePuzzleTest):
    def __init__(self):
        path = os.path.split(inspect.getfile(puzzle))[0]
        data_path = os.path.join(path, "puzzle_data.txt")
        config_path = os.path.join(path, "test_puzzle_config.yaml")

        unit_under_test = puzzle(data_path)
        super().__init__(unit_under_test, config_path)


class TestDemo(BasePuzzleTest):
    def __init__(self):
        path = os.path.split(inspect.getfile(puzzle))[0]
        data_path = os.path.join(path, "demo_data.txt")
        config_path = os.path.join(path, "test_demo_config.yaml")

        unit_under_test = puzzle(data_path)
        super().__init__(unit_under_test, config_path)
