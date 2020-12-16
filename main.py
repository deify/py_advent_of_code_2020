from day01.puzzle import puzzle
import os
import time

if __name__ == "__main__":
    data_path = os.path.join("day13", "puzzle_data.txt")
    uut = puzzle(data_path)
    uut.solve_part2(fps=-1, display=True)
