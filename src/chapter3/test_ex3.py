import unittest
from chapter3.ex3 import is_valid_iban

class TestIbanValidation(unittest.TestCase):
    def test_valid_iban(self):
        # Test met een geldig IBAN-nummer
        self.assertTrue(is_valid_iban("NL91ABNA0417164300"))


    def test_invalid_iban_length(self):
        # Test met een IBAN van onjuiste lengte
        self.assertFalse(is_valid_iban("NL91ABNA04171643"))


    def test_invalid_iban_structure(self):
        # Test met een IBAN met een verkeerde structuur
        self.assertFalse(is_valid_iban("NLABABNA0417164300"))


    def test_invalid_iban_checksum(self):
        # Test met een IBAN met een foutief controlegetal
        self.assertFalse(is_valid_iban("NL92ABNA0417164300"))


    def test_valid_iban_with_spaces(self):
        # Test met een geldig IBAN maar met spaties
        self.assertTrue(is_valid_iban("NL91 ABNA 0417 1643 00"))


if __name__ == '__main__':
    unittest.main()