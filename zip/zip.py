"""
Функция zip() - возвращает список кортежей. Кортеж состоит из i-ых элементов всех итерируемых
объектов, переданных в zip() в качестве параметров.

a = zip([1,2,3], [9,8,7])
list(a) --> [(1, 9), (2, 8), (3, 7)]

b = zip([1,2,3], 'Top')
list(b) --> [(1, 'T'), (2, 'o'), (3, 'p')]

my_list = [[1,2,3], [4,5,6], [7,8,9]]
c = zip(*my_list)
list(c) --> [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

Если длина переданных в функцию zip() аргументов разная, то результат будет выравнен
по длине наименьшего из них:

d = zip([1,2,3,4,5,6], 'CAT')
list(d) --> [(1, 'C'), (2, 'A'), (3, 'T')]
"""


def main():
    students, subjects = list(map(int, input().split()))
    marks = list()

    for i in range(subjects):
        marks.append(list(map(float, input().split())))

    marks_grouped_by_students = list(zip(*marks))

    for i in marks_grouped_by_students:
        result = sum(i) / len(i)
        print(round(result, 1))


if __name__ == '__main__':
    main()
