# print('hello pyCharm')

def sum_pairs(ints, s):
    resultPair = None
    currentList = list(ints)

    def iterateList(list, needSum):
        nonlocal resultPair, currentList

        if currentList:

            for i in range(len(list)):
                for j in range(i+1, len(list)):
                    if list[i]+list[j] == needSum:
                        resultPair = [list[i], list[j]]
                        currentList = currentList[i+1:j]
                        return iterateList(currentList, needSum)

    iterateList(currentList, s)

    return resultPair


print(sum_pairs([10, 5, 2, 8, 3, 7, 5],10))

# работает, но на больших входных списках отваливается по таймауту, сложность O(n^2)
# переделать на сложность O(n)