import unittest
import re
from Function import PhoneValidation

class TestPhoneValidation(unittest.TestCase):

    def setUp(self):
        self.phone_validator = PhoneValidation()

    def test_valid_number(self):
        # Тест на валидный номер телефона
        result = self.phone_validator.validate_phone_numbers('data/test_data.txt')
        self.assertIn('+12345678900', result)

    def test_invalid_number(self):
        # Тест на невалидный номер телефона
        result = self.phone_validator.validate_phone_numbers('data/test_data.txt')
        self.assertNotIn('invalid_number', result)

    def test_empty_file(self):
        # Тест на пустой файл
        result = self.phone_validator.validate_phone_numbers('data/empty_file.txt')
        self.assertEqual(result, [])

    def test_non_numeric_input(self):
        # Тест на неканонический ввод
        result = self.phone_validator.validate_phone_numbers('data/non_numeric_input.txt')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
