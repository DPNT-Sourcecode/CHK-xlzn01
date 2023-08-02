import unittest

from lib.solutions.HLO import hello_solution


class TestHello(unittest.TestCase):
    def test_returns_a_string(self):
        self.assertTrue(isinstance(hello_solution.hello(""), str))

    def test_returns_a_hello_string(self):
        self.assertIn("hello", hello_solution.hello("").lower())

    def test_returns_hello_with_friend_name(self):
        friend_name: str = "John"

        self.assertEquals(f"Hello, {friend_name}!", hello_solution.hello(friend_name=friend_name))

    def test_raises_error_when_null_friend_name(self):
        with self.assertRaises(AssertionError):
            hello_solution.hello(friend_name=None)

