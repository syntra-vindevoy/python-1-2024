import unittest
from example import *

class TestExample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(2.5, 1.5), 1.0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(1.5, 2), 3.0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(1.5, 0.5), 3.0)
        with self.assertRaises(ValueError):
            divide(1, 0)

def run_selected_tests(test_names):
    suite = unittest.TestSuite()
    for test_name in test_names:
        suite.addTest(TestExample(test_name))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def menu():
    test_methods = [method for method in dir(TestExample) if method.startswith('test_')]
    print("Select the test suite to run:")
    for i, test in enumerate(test_methods, 1):
        print(f"{i}. {test.replace('_', ' ').title()}")
    print(f"{len(test_methods) + 1}. Test All (default)")

    choice = input(f"Enter your choice (1-{len(test_methods) + 1}): ")

    if choice.isdigit() and 1 <= int(choice) <= len(test_methods):
        tests_to_run = [test_methods[int(choice) - 1]]
    elif choice == str(len(test_methods) + 1) or choice == '':
        tests_to_run = test_methods
    else:
        print("Invalid choice")
        return
    

    run_selected_tests(tests_to_run)

if __name__ == '__main__':
    menu()