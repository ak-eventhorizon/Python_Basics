import re


def validate_credit_card(s: str) -> bool:
    """
    Check if string is valid Credit Card number

    A valid credit card has the following characteristics:
    1) It must start with a 4 ,5 or 6.
    2) It must contain exactly 16 digits.
    3) It must only consist of digits (0-9).
    4) It may have digits in groups of 4, separated by one hyphen "-".
    5) It must NOT use any other separator like ' ' , '_', etc.
    6) It must NOT have 4 or more consecutive repeated digits.

    :param s:
    :return:
    """

    structure_pattern = r'[456]\d{3}(-?\d{4}){3}$'
    not_repeat_pattern = r'((\d)-?(?!(-?\2){3})){16}'
    filters = structure_pattern, not_repeat_pattern

    if all(re.match(f, s) for f in filters):
        return True
    else:
        return False


if __name__ == '__main__':

    inputs = ['4253625879615786',
              '4424424424442444',
              '5122-2368-7954-3214',
              '4253625879615786723456789',
              '4424444424442444',
              '5122-2368-7954 - 3214',
              '44244x44A4442444',
              '0525362587961578']

    for i in inputs:
        if validate_credit_card(i):
            print('Valid')
        else:
            print('Invalid')
