import unittest
from src.fizz_buzz import *

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.number1 = 23
        self.number2 = 9
        self.number3 = 25
        self.number4 = 30

    def test_fizz_buzz_return_number(self):
        self.assertEqual("23",fizz_buzz(self.number1))
        

    def test_fizz_buzz_return_Fizz(self):
        self.assertEqual("Fizz",fizz_buzz(self.number2))

    def test_fizz_buzz_return_Buzz(self):
         self.assertEqual("Buzz",fizz_buzz(self.number3))

    def test_fizz_buzz_return_FizzBuzz(self):
        self.assertEqual("FizzBuzz",fizz_buzz(self.number4))