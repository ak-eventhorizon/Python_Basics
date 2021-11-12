"""
You are given some information about  people.
Each person has a first name, last name, age and sex.
Print their names in a specific format sorted by their age in ascending order
i.e. the youngest person's name should be printed first.
For two people of the same age, print them in the order of their input.

Sample Input:

Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Sample Output:

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
"""
from operator import itemgetter


def person_lister(func):
    def inner(*args):
        peoples = args[0]
        peoples.sort(key=itemgetter(2))  # сотрировка на месте по третьему элементу в списке (возраст)
        result = list()

        for person in peoples:
            result.append(func(person))

        return result
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1] + " (" + person[2] + ")"


if __name__ == '__main__':
    people = [['Mike', 'Thomson', '20', 'M'],
              ['Robert', 'Bustle', '32', 'M'],
              ['Andria', 'Bustle', '30', 'F'],
              ['Tom', 'Hardy', '56', 'M'],
              ['Markus', 'Herbert', '11', 'M'],
              ['Maria', 'Esposito', '17', 'F'],
              ['Tobias', 'Fredrik', '89', 'M'],
              ['Helen', 'Heller', '30', 'F']]

    print(*name_format(people), sep='\n')
