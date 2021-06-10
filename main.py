# print('hello pyCharm')

def sum_pairs(ints, s):
    seenYouBefore = set()

    for num in ints:
        difference = s - num

        if num in seenYouBefore:
            return [difference, num]

        seenYouBefore.add(difference)

    return None


print(sum_pairs([10, 5, 2, 8, 3, 7, 5],10))

# работает, но на больших входных списках отваливается по таймауту, сложность O(n^2)
# переделать на сложность O(n)