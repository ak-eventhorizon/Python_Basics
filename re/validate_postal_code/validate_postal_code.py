"""
A valid postal code  have to fullfil both below requirements:

- must be a number in the range from 100000 to 999999 inclusive (first regex)
- must not contain more than one alternating repetitive digit pair (second regex)

121426
^ ^     - alternating repetitive digit pair

552523
 ^*^*   - two alternating repetitive digit pair

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.

"""

if __name__ == '__main__':

    import re

    regex_integer_in_range = r"^[1-9][\d]{5}$"
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

    P = input()

    print(bool(re.match(regex_integer_in_range, P))
          and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
