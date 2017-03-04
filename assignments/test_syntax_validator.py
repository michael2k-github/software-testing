import unittest
import syntax_validator

class test_syntax_validator(unittest.TestCase):

    """
    Tests to validate username
    """
    def test_is_valid_username_returns_true_given_valid_input(self):
        self.assertTrue(syntax_validator.is_valid_username('Abcdefg1'))

    def test_is_valid_username_returns_false_given_invalid_input(self):
        self.assertFalse(syntax_validator.is_valid_username('abcdefg1'))

    """
    Additional tests to validate username
    """
    def test_username_is_too_long_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_username('Ab3456789ABCD'))

    def test_username_is_too_short_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_username('Ab34567'))

    def test_username_is_all_caps_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_username('ABCDEFGH'))

    def test_username_is_all_digits_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_username('12345678'))

    def test_username_ends_with_punctions_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_username('Abcdefg8!'))

    def test_username_is_not_valid_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_username('Ab3 -Ab3 _?'))

    def test_username_is_all_punctions_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_username('!,.$;:-?'))

    def test_username_is_all_spaces_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_username('        '))

    def test_username_is_blank_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_username(''))

    def test_username_single_alpha_returns_true(self):
        self.assertTrue(syntax_validator.is_valid_username('A2345678'))

    def test_username_has_mixed_letter_bookends_returns_true(self):
        self.assertTrue(syntax_validator.is_valid_username('A2345678b'))

    def test_username_has_cap_letter_bookends_returns_true(self):
        self.assertTrue(syntax_validator.is_valid_username('A2345678B'))

    def test_username_has_single_letter_returns_true(self):
        self.assertTrue(syntax_validator.is_valid_username('A2345678'))

    def test_username_is_all_caps_returns_true(self):
        self.assertTrue(syntax_validator.is_valid_username('ABCDEFG1'))

    """
    Tests to validate zip code
    """
    def test_is_valid_us_zip_code_returns_true_given_valid_input(self):
        self.assertTrue(syntax_validator.is_valid_us_zip_code('55555'))

    def test_is_valid_us_zip_code_returns_false_given_invalid_input(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('5555'))
    """
    Additional tests to validate zip code
    """
    def test_is_too_long_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('123456'))

    def test_is_too_long_full_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('123456-7890'))

    def test_is_too_long_extension_full_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('12345-67890'))

    def test_is_too_many_zip_extension_full_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('12345-12345-0123'))

    def test_is_too_many_zip_and_extension_full_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('12345-6789-12345-0123'))

    def test_is_too_many_extension_full_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('12345-6789-0123'))

    def test_is_dashes_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('-----'))

    def test_is_short_alpha_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('abcde'))

    def test_is_ended_alpha_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('12345b'))

    def test_is_bookended_alpha_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('a12345b'))

    def test_is_long_alpha_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('abcde-efgi'))

    def test_is_all_blank_returns_false(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code(''))

    def test_is_all_zeroes_short_returns_true(self):
        self.assertTrue(syntax_validator.is_valid_us_zip_code('00000'))

    def test_is_all_zeroes_full_returns_true(self):
        self.assertTrue(syntax_validator.is_valid_us_zip_code('00000-0000'))
