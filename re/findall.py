import re


if __name__ == '__main__':
    my_string = 'List was Madre for purpose of YA Real -- rock N Roll U'

    pattern1 = re.compile(r'([A-Z]\w+)')
    pattern2 = re.compile(r'([A-Z]\w*)')
    result1 = pattern1.findall(my_string)
    result2 = pattern2.findall(my_string)

    print('Pattern 1: ', result1)
    print('Pattern 2: ', result2)
