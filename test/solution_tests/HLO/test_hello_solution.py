import unittest

from lib.solutions.HLO import hello_solution


class TestHello(unittest.TestCase):
    def test_returns_a_string(self):
        self.assertTrue(isinstance(hello_solution.hello(""), str))

    def test_returns_a_hello_string(self):
        self.assertIn("hello", hello_solution.hello("").lower())

    def test_returns_hello_world_regardless(self):
        self.assertEqual(hello_solution.hello(""), "Hello, World!")
