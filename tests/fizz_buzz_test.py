import unittest
from src.fizz_buzz import *

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.number1 = 7
        self.number2 = 9
        self.number3 = 25
        self.number4 = 30
        self.number5 = 59

    def test_fizz_buzz_return_ruzz(self):
        self.assertEqual("Ruzz",fizzbuzz(self.number1))
        
    def test_fizz_buzz_return_Fizz(self):
        self.assertEqual("Fizz",fizzbuzz(self.number2))

    def test_fizz_buzz_return_Buzz(self):
         self.assertEqual("Buzz",fizzbuzz(self.number3))

    def test_fizz_buzz_return_FizzBuzz(self):
        self.assertEqual("FizzBuzz",fizzbuzz(self.number4))

    def test_fizz_buzz_return_number(self):
        self.assertEqual("59",fizzbuzz(self.number5))