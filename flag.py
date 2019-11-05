import sys

class Validator:
    validate_queue = ('type', 'positive', 'even')
    error_messages = {
        'type_error': 'Value should be integer number ',
        'positive_error': 'Value should be positive number',
        'even_error': 'Value is not an even number.',
    }

    def __init__(self, n):
        self.n = n

    def validate(self):
        for validate_type in self.validate_queue:
            if not getattr(self, f'{validate_type}_validation')():
                raise ArgumentError(
                    self.error_messages[f'{validate_type}_error']
                )

    def type_validation(self):
        return isinstance(self.n, int)

    def positive_validation(self):
        return self.n > 0

    def even_validation(self):
        return not self.n % 2


class ArgumentError(Exception):
    pass


def flag(n):
    v = Validator(n)
    v.validate()
    flag_border = '#'
    circle_border = '*'
    inner_circle = 'o'
    height_coefficient = 2
    width_coefficient = 3
    width = n * width_coefficient + 2
    height = n * height_coefficient + 2
    flag = ''
    for line_pointer in range (height // 2):
        line = ''
        for row_pointer in range(width // 2):
            if row_pointer == 0 or row_pointer == width - 1 or line_pointer == 0 or line_pointer == height - 1:
                line += flag_border
            elif line_pointer + row_pointer == 2 * n + 1:
                line += circle_border
            elif line_pointer + row_pointer > 2 * n + 1:
                line += inner_circle
            else:
                line += ' '
        flag += (line + line[::-1] + '\n')
    return flag[:-1] + flag[::-1]

try:
	n = 6
	print('N = ' + str(n) + '\n' + flag(n))
except ArgumentError as exp:
    print('Exception : ' + str(exp))