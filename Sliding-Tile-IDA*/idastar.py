"""
IDA* Algorithm is implemented in this file.
Algorithm uses State class for operations.
"""
from state import State
from typing import List, Tuple, Optional
from copy import deepcopy
import numpy as np


# Implement the IDA* algrothism to solve the puzzle when puzzle is solvable
def ida_star(state: State) -> Optional[State]:
    if not state.is_solvable:
        return None

    upper_bound = state.this_distance
    while True:
        result = search(state, 0, upper_bound, [])
        if result[0] == -1:
            return result[1]
        elif result[0] == 1000:
            return None
        upper_bound = result[0]
        
# Try different bound to find the min step for solution
def search(state: State, goal_value: int, upper_bound: int, previous: List[np.array]) -> Tuple[int, Optional[State]]:
    if goal_value > 31:
        return 1000, None

    if state.get_distance() == 0:
        print_helper(state.this_state.take(0, axis=2).flatten())
        for arr in reversed(previous):
            print_helper(arr)
        return -1, state
    f_value = goal_value + state.this_distance
    if f_value > upper_bound:
        return f_value, None
    min_value = 1000
    for i in range(4):
        in_state = deepcopy(state)
        if in_state.gen_next_state(i):
            previous_deep = deepcopy(previous)
            previous_deep.append(state.this_state.take(0, axis=2).flatten())
            result = search(in_state, goal_value + 1, upper_bound, previous_deep)
            if result[0] == -1:
                return result
            min_value = min(min_value, result[0])
    return min_value, None

#This function is use to print the solve step
def print_helper(arr: np.array):
    print_string = ''
    for i in range(9):
        print_string += str(arr[i]) + ' '
        if (i + 1) % 3 == 0:
            print_string += '\n'
    print(print_string)