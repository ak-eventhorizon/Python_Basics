# print('hello pyCharm')

students_marks = {'Krishna': [67, 68, 69], 'Arjun': [70, 98, 63], 'Malika': [52, 56, 60]}

query_name = 'Malika'

if query_name in students_marks:
    result = sum(students_marks[query_name]) / len(students_marks[query_name])
    print(format(result, '.2f'))
