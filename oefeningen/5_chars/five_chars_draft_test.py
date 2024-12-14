import unittest
from five_chars_draft import has_forbidden_char

class Test5CharsDraft(unittest.TestCase):

    def test_has_forbidden_char(self):
        self.assertTrue(has_forbidden_char("aeiou", "hello"))
        self.assertFalse(has_forbidden_char("xyz", "hello"))
        self.assertTrue(has_forbidden_char("h", "hello"))
        self.assertFalse(has_forbidden_char("z", "hello"))
        self.assertTrue(has_forbidden_char("aeiou", "umbrella"))
        self.assertFalse(has_forbidden_char("xyz", "umbrella"))

if __name__ == "__main__":
    unittest.main()