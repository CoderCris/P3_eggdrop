import unittest

from ks_utils     import *
from solve_tabulation import *
from solve_memoization import *
import numpy as np

class TestKSP(unittest.TestCase):

    def test_higherVal(self):
        content = """40 20"""
        eggs_num, floors = from_data_to_items(content)
        check_solution(eggs_num, floors)