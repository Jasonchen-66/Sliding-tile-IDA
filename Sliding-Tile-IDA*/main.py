"""
Input file creation functions and main part are implemented in this file.
To run, just type "python3 main.py" into the Console.
"""
import sys
from state import State
from typing import Tuple, List
from idastar import ida_star


#Read the input file and store the first 3 lines as inital puzzle state and last 3 lines as goal puzzle state
def take_input() -> State:
    with open('inputPuzzle.txt', 'r') as input_puzzle:
        goal: List[Tuple[int, int, int]] = []
        for _ in range(3):
            goal.append(tuple(map(lambda x: int(x), input_puzzle.readline().split())))

        input_puzzle.readline()

        initial: List[Tuple[int, int, int]] = []
        for _ in range(3):
            initial.append(tuple(map(lambda x: int(x), input_puzzle.readline().split()))
                           )
    return State(initial, goal)



#Run the whole program, open the input puzzle and write the solution to outputIDA.txt
if __name__ == '__main__':
    print('Running...')
    state: State = take_input()
    result = ida_star(state)
    if result is None:
        print('This puzzle is not solveable.')
    else:
        print('Puzzle solved.')
