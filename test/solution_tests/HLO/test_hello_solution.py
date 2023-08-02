import unittest

from lib.solutions.HLO import hello_solution

class TestHello(unittest.TestCase):
    def test_returns_a_string(self):
        self.assertTrue(isinstance(hello_solution.hello(""), str))