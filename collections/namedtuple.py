from collections import namedtuple
"""
Point = namedtuple('Point', 'x y')
pt1 = Point(1, 4)
pt2 = Point(2, 6)

К содержимому такого контейнера можно обращаться как по индексу, так и по имени.

print(pt1) -> Point(x=1, y=4)
print(pt1[1]) -> 4
print(pt1.x + pt2.y) -> 7
"""


# это решение проще читать
def approach_1():
    num_of_studs = int(input('Number of students: '))
    Student = namedtuple('Student', input('Fields order: ').split())  # ID NAME CLASS MARKS - any order
    sum_of_marks = 0

    for i in range(num_of_studs):
        usr_input = input(f'Student {i}: ').split()
        # stud = Student(usr_input[0], usr_input[1], usr_input[2], usr_input[3])
        stud = Student(*usr_input)
        sum_of_marks += int(stud.MARKS)

    print('{:.2f}'.format(sum_of_marks / num_of_studs))


# это решение более лаконичное, но сложнее воспринимается
def approach_2():
    num, Student = int(input()), namedtuple('Student', input().split())
    sum_of_marks = [Student(*input(f'Student {i}: ').split()).MARKS for i in range(num)]
    print('{:.2f}'.format(sum(map(int, sum_of_marks)) / num))


if __name__ == '__main__':
    approach_1()
