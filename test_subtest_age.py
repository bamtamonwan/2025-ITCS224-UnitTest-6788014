import unittest

# This is the function we are testing
def get_age_category(age):
    if 0 <= age <= 9:
        return "child"
    elif 18 <= age <= 64:
        return "adult"
    elif age >= 65:
        return "senior"
    return "unknown"

class TestSubtestAge(unittest.TestCase):

    def test_child_age(self):
        """Tests ages 0 through 9 for the child category"""
        for age in range(10):  # 0 to 9
            with self.subTest(age=age):
                print(f"{age} is considered as a child.")
                self.assertEqual(get_age_category(age), "child")

    def test_adult_age(self):
        """Tests ages 18 through 20 for the adult category"""
        # We use a smaller range (18-20) here for brevity in output
        for age in range(18, 21): 
            with self.subTest(age=age):
                print(f"{age} is considered as an adult.")
                self.assertEqual(get_age_category(age), "adult")

    def test_senior_age(self):
        """Tests ages 65 through 67 for the senior category"""
        for age in range(65, 68):
            with self.subTest(age=age):
                print(f"{age} is considered as a senior.")
                self.assertEqual(get_age_category(age), "senior")

if __name__ == '__main__':
    unittest.main()