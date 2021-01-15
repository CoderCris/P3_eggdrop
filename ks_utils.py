from solve_tabulation import *
from solve_memoization import *


# Routine used in my_tests.py to read input-data from a string!
def from_data_to_items(input_data):
    lines = input_data.split('\n')

    first_line = lines[0].split()
    eggs_num = int(first_line[0])
    floors = int(first_line[1])

    return eggs_num, floors

def check_solution(eggs_num, floors):
    mem = solve_memoization(eggs_num, floors)
    tab = solve_tabulation(eggs_num, floors)
    print("¿coinciden los métodos Tabulation y Memoization?", mem[eggs_num, floors] == tab[eggs_num][floors])
