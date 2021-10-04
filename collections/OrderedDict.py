from collections import OrderedDict
"""
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. 
If a new entry overwrites an existing entry, the original insertion position is left unchanged.

>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
"""


def calc_items_sum_price() -> None:

    ordered_dict = OrderedDict()
    count = int(input("Count: "))

    for i in range(count):
        usr_input = input().split()

        item_name = ' '.join(usr_input[:-1])
        net_price = int(usr_input[-1])

        if item_name not in ordered_dict.keys():
            ordered_dict[item_name] = net_price
        else:
            ordered_dict[item_name] += net_price

    for key, value in ordered_dict.items():
        print(key, value)


if __name__ == '__main__':
    calc_items_sum_price()

# ----- INPUT: -----
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

# ----- OUTPUT: -----
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20