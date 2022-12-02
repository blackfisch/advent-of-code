"""
AoC 2022 Day 2: Rock Paper Scissors
https://adventofcode.com/2022/day/2
"""

from aocd import data

class RPS:
    """Rock Paper Scissors class"""
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    WIN = 6
    DRAW = 3
    LOSE = 0

    RPS_VALUES = {
        "A": ROCK,  
        "B": PAPER,  
        "C": SCISSORS,  

        "X": ROCK,  
        "Y": PAPER,  
        "Z": SCISSORS
    }

    def __init__(self, data: str):
        self.data = self.parse_data(data)

    def parse_data(self, data: str) -> list:
        """Parse data"""

        return [list(map(lambda el: self.RPS_VALUES.get(el, -1), game.split(" ")))
                for game in data.splitlines()]

    def winner_points(self, user_a: int, user_b: int) -> int:
        win_points = self.LOSE 

        if user_a == user_b:
            win_points = self.DRAW
        elif user_a == self.ROCK and user_b == self.SCISSORS:
            pass
        elif (user_a == self.SCISSORS and user_b == self.ROCK) or user_a < user_b:
            win_points = self.WIN

        return (win_points + user_b)


    def solve_a(self) -> int:
        """RPS solver part A"""
        return sum(self.winner_points(*pair) for pair in self.data)


### Solutions ###

def part_a(data: str):
    """Solution for part A"""
    return RPS(data).solve_a()



def part_b(data: str):
    """Solution for part B"""
    pass


if __name__ == '__main__':
    print(f'Part A: {part_a(data)}')
    print(f'Part B: {part_b(data)}')
