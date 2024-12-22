import unittest
import sys
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
        suite.addTest(TestExample(f"test_{test_name}"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def menu():
    test_methods = [method for method in dir(TestExample) if method.startswith('test_')]
    test_names = [method[5:] for method in test_methods]  # Remove 'test_' prefix for display
    print("Select the test suite to run:")
    print(f"0. Test All (default)")
    for i, test in enumerate(test_names, 1):
        print(f"{i}. {test.replace('_', ' ').title()}")

    choice = input(f"Enter your choice (1-{len(test_names) + 1}): ")

    if choice == '0' or choice == '':
        tests_to_run = test_names
    elif choice.isdigit() and 1 <= int(choice) <= len(test_names):
        tests_to_run = [test_names[int(choice) - 1]]
    else:
        print("Invalid choice")
        return

    run_selected_tests(tests_to_run)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Run specific tests provided as command-line arguments without 'test_' prefix
        tests_to_run = [arg for arg in sys.argv[1:]]
        run_selected_tests(tests_to_run)
    else:
        # Run all tests if no arguments are provided
        menu()