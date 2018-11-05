import sys

from src.wrong_key_exception import WrongKeyException


class ValidCreatorFourNumberKey(object):

    def __init__(self, first_4_digits, last_4_digits, my_birth_date, last_key = '0000'):
        self.first_4_digits = first_4_digits
        self.last_4_digits = last_4_digits
        self.year, self.month, self.day = my_birth_date.split('/')
        self.last_key = last_key
        self.values = []

    def run(self):
        for x in range(10000):
            value = self.create_valid_format_str_value(x)
            if self.is_valid(value):
                self.values.append(value)
        self.print_all_valid_values()

    def print_all_valid_values(self):
        print self.values[0:1000]
        print self.values[1000:2000]
        print self.values[2000:3000]
        print self.values[3000:4000]
        print self.values[4000:5000]
        print self.values[5000:6000]
        print self.values[6000:7000]
        print self.values[7000:8000]
        print self.values[8000:9000]
        print self.values[9000:10000]

    def create_valid_format_str_value(self, x):
        value_str = str(x)
        if len(value_str) == 1:
            value_str = '000' + value_str
        elif len(value_str) == 2:
            value_str = '00' + value_str
        elif len(value_str) == 3:
            value_str = '0' + value_str
        return value_str

    def is_valid(self, value):
        try:
            self.evaluate_last_key(value)
            self.evaluate_repeated_numbers( value)
            self.is_valid_if_not_contains_consecutive_numbers(value)
            self.is_valid_if_not_first_or_last_document(value)
            self.is_valid_if_not_start_with_19_nor_20(value)
            return True
        except WrongKeyException as we:
            print str(we)
            return False


    def evaluate_last_key(self, value):
        if (value == self.last_key):
            raise WrongKeyException('New Key is equal than last key for value : %s' % value)
        return True

    def evaluate_repeated_numbers(self, value):
        is_valid = True
        range_validator = list(map(lambda x: str(x), range(10)))
        increment = 0
        while is_valid and increment < 10:
            evaluator = range_validator[increment]
            checker = filter((lambda x: x == evaluator), value)
            is_valid = len(checker) <= 3
            if is_valid:
                increment += 1
            else:
                raise WrongKeyException('You sent some number repeated more than three times for value : %s' % value)
        return True

    def is_valid_if_not_contains_consecutive_numbers(self, to_evaluate):
        first, second, third, fourth = list(map(lambda x: int(x), to_evaluate))
        first_to_second = (second == first + 1)
        second_to_third = (third == second + 1)
        third_to_fourth = (fourth == third + 1)
        first_to_third_consecutives = first_to_second and second_to_third
        second_to_fourth_consecutives = second_to_third and third_to_fourth
        if first_to_third_consecutives or second_to_fourth_consecutives:
            raise WrongKeyException('You sent a key with consecutives values for value : %s' % to_evaluate)
        return True

    def is_valid_if_not_first_or_last_document(self, to_evaluate):
        if to_evaluate == self.first_4_digits:
            raise WrongKeyException('You sent a a value equals your first four digits from your doc for value : %s' % to_evaluate)
        if to_evaluate == self.last_4_digits:
            raise WrongKeyException('You sent a a value equals your last four digits from your doc for value : %s' % to_evaluate)
        return True

    def is_valid_if_not_start_with_19_nor_20(self, to_evaluate):
        if to_evaluate[0:2] in ["19", '20']:
            raise WrongKeyException('You should not sent a number starting with 19 nor 20 for value : %s' % to_evaluate)
        return True

    def is_valid_if_not_contains_birthday_data(self, to_evaluate):
        self.evaluate_year(to_evaluate)
        self.evaluate_month_day(to_evaluate)
        self.evaluate_month_year(to_evaluate)
        return True

    def evaluate_year(self, to_evaluate):
        if to_evaluate == self.year:
            raise WrongKeyException('You sent a value equals your birthday year for value : %s' % to_evaluate)

    def evaluate_month_day(self, to_evaluate):
        day_month = (to_evaluate == (self.day + self.month))
        month_day = (to_evaluate == (self.month + self.day))
        if day_month or month_day:
            raise WrongKeyException('You sent a value with your birthday day and month for value : %s' % to_evaluate)

    def evaluate_month_year(self, to_evaluate):
        year_month = (to_evaluate == (self.year[2:4] + self.month))
        month_year = (to_evaluate == (self.month + self.year[2:4]))
        if year_month or month_year:
            raise WrongKeyException('You sent a a value with your birthday year and month for value : %s' % to_evaluate)

if __name__ == '__main__':
    if len(sys.argv) < 5:
        first_4 = raw_input("ingrese los primeros 4 digitos de su documento:\n")
        last_4 = raw_input("ingrese los ultimos 4 digitos de su documento:\n")
        birthay = raw_input("ingrese la fecha de su cumpleanios(yyyy/mm/dd):\n")
        old_key = raw_input("ingrese la clave deprecada:\n")
    else:
        first_4 = sys.argv[1]
        last_4 = sys.argv[2]
        birthay = sys.argv[3]
        old_key = sys.argv[4]
    ValidCreatorFourNumberKey(first_4, last_4, birthay, old_key).run()