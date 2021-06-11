# print('hello pyCharm')

def sum_pairs(ints, s):
    seen_you_before = set()

    for num in ints:
        difference = s - num

        if num in seen_you_before:
            return [difference, num]

        seen_you_before.add(difference)

    return None


print(sum_pairs([10, 5, 2, 8, 3, 7, 5], 10))
