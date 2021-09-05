def count_substring(string, sub_string):
    counter = 0
    sub_string_len = len(sub_string)

    for i in range(len(string)):
        if string[i:i + sub_string_len] == sub_string:
            counter += 1

    return counter


print(count_substring('ABCDCDC', 'CDC'))
