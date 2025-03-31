import unittest

from src.OO.developer import Developer


class TestDeveloper(unittest.TestCase):
    def setUp(self):
        self.dev = Developer("John", "Doe", 50000)

    def test_init(self):
        self.assertEqual(self.dev.first, "John")
        self.assertEqual(self.dev.last, "Doe")
        self.assertEqual(self.dev.pay, 50000)
        self.assertEqual(self.dev.prog_langs, [])

    def test_add_prog_lang(self):
        self.dev.add_prog_lang("Python")
        self.assertEqual(self.dev.prog_langs, ["Python"])
        self.dev.add_prog_lang("Java")
        self.assertEqual(self.dev.prog_langs, ["Python", "Java"])

    def test_remove_prog_lang(self):
        # Test removing existing language
        self.dev.add_prog_lang("Python")
        self.dev.remove_prog_lang("Python")
        self.assertEqual(self.dev.prog_langs, [])

        # Test removing non-existing language
        self.dev.remove_prog_lang("Java")  # Should not raise error
        self.assertEqual(self.dev.prog_langs, [])

    def test_apply_raise(self):
        initial_pay = self.dev.pay
        self.dev.apply_raise()
        self.assertAlmostEqual(self.dev.pay, initial_pay * self.dev.raise_amt, places=2)

    def test_str_representation(self):
        self.dev.add_prog_lang("Python")
        self.dev.add_prog_lang("Java")
        str_repr = str(self.dev)
        self.assertIn("John", str_repr)
        self.assertIn("Doe", str_repr)
        self.assertIn("Python", str_repr)
        self.assertIn("Java", str_repr)

    def test_repr_representation(self):
        self.dev.add_prog_lang("Python")
        repr_str = repr(self.dev)
        self.assertIn("John", repr_str)
        self.assertIn("Doe", repr_str)
        self.assertIn("Python", repr_str)


if __name__ == '__main__':
    unittest.main()
