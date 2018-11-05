import os
from unittest import TestCase
import subprocess as sb

from src.valid_creator_four_number_key import ValidCreatorFourNumberKey


class ValidCreatorFourNumberKeyTest(TestCase):

    def test_when_run_i_should_create_valid_list_black_box(self):
        with open("my_keys.txt", 'w') as keys:
            sb.call(['python', '../src/valid_creator_four_number_key.py', '2120', '2120', '1975/20/11', '2010'], stdout=keys)
        with open("my_keys.txt", 'r') as keys:
            values = keys.readlines()
        self.assertEqual(373, len(values))

    def test_when_run_i_should_create_valid_list(self):
        number_creator = ValidCreatorFourNumberKey('1111', '9999', '1913/07/03')
        list_values = number_creator.values
        self.assertTrue("0000" not in list_values)
        self.assertTrue("0123" not in list_values)


    def test_when_i_receieve_a_number_I_should_convert_it_to_valid_str_with_one_digit(self):
        number_creator = ValidCreatorFourNumberKey('1111', '9999', '1913/07/03')
        result = number_creator.create_valid_format_str_value(0)
        self.assertEqual('0000', result)

    def test_when_i_receieve_a_number_I_should_convert_it_to_valid_str_with_two_digit(self):
        number_creator = ValidCreatorFourNumberKey('1111', '9999', '1913/07/03')
        result = number_creator.create_valid_format_str_value(10)
        self.assertEqual('0010', result)

    def test_when_i_receieve_a_number_I_should_convert_it_to_valid_str_with_three_digit(self):
        number_creator = ValidCreatorFourNumberKey('1111', '9999', '1913/07/03')
        result = number_creator.create_valid_format_str_value(100)
        self.assertEqual('0100', result)

    def test_when_i_receieve_a_number_I_should_convert_it_to_valid_str_with_four_digit(self):
        number_creator = ValidCreatorFourNumberKey('1111', '9999', '1913/07/03')
        result = number_creator.create_valid_format_str_value(9100)
        self.assertEqual('9100', result)

    def test_when_if_last_key_is_equal_than_last_key_should_raise_exception(self):
        number_creator = ValidCreatorFourNumberKey('1111', '9999', '1913/07/03', '1234')
        self.evaluate_condition((lambda:number_creator.evaluate_last_key('1234'))
                                , 'New Key is equal than last key')


    def test_when_i_sent_a_value_with_more_than_three_zeros_should_not_be_valid(self):
        number_creator = ValidCreatorFourNumberKey('1111', '9999', '1913/07/03')
        expected_error_msg = 'You sent some number repeated more than three times'
        values_wrongs = ['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999']
        for value in values_wrongs:
            self.evaluate_condition((lambda: number_creator.evaluate_repeated_numbers(value))
                                    , expected_error_msg)

    def test_when_i_sent_a_value_with_consecutive_numbers_should_not_be_valid(self):
        number_creator = ValidCreatorFourNumberKey('1111', '9999', '1913/07/03')
        expected_error_msg = 'You sent a key with consecutives values'
        values_wrongs = ['1230', '0123']
        for value in values_wrongs:
            self.evaluate_condition((lambda: number_creator.is_valid_if_not_contains_consecutive_numbers(value))
                                    , expected_error_msg)


    def test_when_i_sent_a_value_equals_first_4digit_should_raise_exc(self):
        number_creator = ValidCreatorFourNumberKey('2010', '1242', '1913/07/03')
        self.evaluate_condition((lambda: number_creator.is_valid_if_not_first_or_last_document('2010'))
                                , 'You sent a a value equals your first four digits from your doc')

    def test_when_i_sent_a_value_equals_last_4digit_should_raise_exc(self):
        number_creator = ValidCreatorFourNumberKey('2010', '1242', '1913/07/03')
        self.evaluate_condition((lambda: number_creator.is_valid_if_not_first_or_last_document('1242'))
                                , 'You sent a a value equals your last four digits from your doc')

    def test_when_i_sent_a_value_starting_with_19_or20_should_not_be_valid(self):
        number_creator = ValidCreatorFourNumberKey('2010', '1242', '1913/07/03')
        expected_error_msg = 'You should not sent a number starting with 19 nor 20'
        values_wrongs = ['1930', '2023']
        for value in values_wrongs:
            self.evaluate_condition((lambda: number_creator.is_valid_if_not_start_with_19_nor_20(value))
                                    , expected_error_msg)

    def test_when_i_sent_a_value_with_birth_year_should_not_be_valid(self):
        number_creator = ValidCreatorFourNumberKey('2010', '1242', '1973/07/03')
        self.evaluate_condition((lambda: number_creator.is_valid_if_not_contains_birthday_data('1973'))
                                , 'You sent a value equals your birthday year')


    def test_when_i_sent_a_value_with_month_day_should_not_be_valid(self):
        number_creator = ValidCreatorFourNumberKey('2010', '1242', '1973/07/03')
        self.evaluate_condition((lambda: number_creator.is_valid_if_not_contains_birthday_data('0703'))
                                , 'You sent a value with your birthday day and month')


    def test_when_i_sent_a_value_with_day_month_should_not_be_valid(self):
        number_creator = ValidCreatorFourNumberKey('2010', '1242', '1973/07/03')
        self.evaluate_condition((lambda: number_creator.is_valid_if_not_contains_birthday_data('0307'))
                                , 'You sent a value with your birthday day and month')

    def test_when_i_sent_a_value_with_month_year_should_not_be_valid(self):
        number_creator = ValidCreatorFourNumberKey('2010', '1242', '1973/07/03')
        self.evaluate_condition((lambda: number_creator.is_valid_if_not_contains_birthday_data('0773'))
                                , 'You sent a a value with your birthday year and month')

    def test_when_i_sent_a_value_with_year_monthshould_not_be_valid(self):
        number_creator = ValidCreatorFourNumberKey('2010', '1242', '1973/07/03')
        self.evaluate_condition((lambda: number_creator.is_valid_if_not_contains_birthday_data('7307'))
                                , 'You sent a a value with your birthday year and month')

    def evaluate_condition(self, my_function, msg_expected):
        try:
            my_function()
            self.fail()
        except Exception as ex:
            self.assertEqual(msg_expected, ex.message)

    def tearDown(self):
        if os.path.exists("my_keys.txt"):
            os.remove("my_keys.txt")