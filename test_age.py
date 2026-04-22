import unittest
from age import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_child(self):
        self.assertEqual(categorize_by_age(5), "Child")

    def test_adolescent(self):
        self.assertEqual(categorize_by_age(15), "Adolescent")

    def test_adult(self):
        self.assertEqual(categorize_by_age(30), "Adult")

    def test_golden_age(self):
        self.assertEqual(categorize_by_age(70), "Golden age")

    def test_negative_age(self):
        self.assertEqual(categorize_by_age(-1), "Invalid age: -1")

    def test_too_old(self):
        self.assertEqual(categorize_by_age(151), "Invalid age: 151")

if __name__ == "__main__":
    unittest.main(verbosity=2)
    def test_boundary_child_adolescent(self):
        self.assertEqual(categorize_by_age(9), "Child")
        self.assertEqual(categorize_by_age(10), "Adolescent")

    def test_boundary_adolescent_adult(self):
        self.assertEqual(categorize_by_age(18), "Adolescent")
        self.assertEqual(categorize_by_age(19), "Adult")

    def test_boundary_adult_golden_age(self):
        self.assertEqual(categorize_by_age(65), "Adult")
        self.assertEqual(categorize_by_age(66), "Golden age")
import unittest

def is_even(number):
    return number % 2 == 0

class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        for number in [2, 4, 6, -8, -10, -12]:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), True)

    def test_odd_number(self):
        for number in [1, 3, 5, -7, -9, -11]:
            with self.subTest(number=number):
                self.assertEqual(is_even(number), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)
