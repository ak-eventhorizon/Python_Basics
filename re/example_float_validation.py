import re


def floating_validator(string: str) -> bool:
    pattern = r'^[-+]?[0-9]*\.[0-9]+$'
    res = re.match(pattern, string)
    return bool(res)


if __name__ == '__main__':
    print(floating_validator('+4.50'))      # True
    print(floating_validator('-1.0'))       # True
    print(floating_validator('.5'))         # True
    print(floating_validator('-.7'))        # True
    print(floating_validator('+.4'))        # True
    print(floating_validator('+-4.5'))      # False
    print(floating_validator('12.'))        # False
    print(floating_validator('12.0'))       # True
    print(floating_validator('12.0.5'))     # False
    print(floating_validator('4.0o0'))      # False
    print(floating_validator('-1.00'))      # True
    print(floating_validator('+4.54'))      # True
    print(floating_validator('Somthn'))     # False
