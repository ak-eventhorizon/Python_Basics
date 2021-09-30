from collections import defaultdict

"""
Обычный словарь Python вернет KeyError, если попытаться получить из него элемент с
ключем, которого нет. 

defaultdict создаст элемент с таким ключем, при попытке получения к нему 
доступа, если такой элемент еще не существует.

Параметр, передаваемый методу defaultdict()...
defaultdict(list)
defaultdict(int)
defaultdict(str)
...определяет, какой тип значений будет по умолчанию у вновь создаваемых элементов этого словаря.

ПРИМЕР:
d1 = defaultdict(int)
d2 = defaultdict(list)

print(d1['first']) -> 0
print(d1) -> defaultdict(<class 'int'>, {'first': 0})

print(d2['first']) -> []
print(d2) -> defaultdict(<class 'list'>, {'first': []})
"""


def main():
    size_a, size_b = input('Size Group A <space> Size Group B: ').split()
    size_a = int(size_a)
    size_b = int(size_b)

    my_dict = defaultdict(list)

    for i in range(1, size_a + 1):
        my_dict['group_a'].append(input(f'{i} word of group A: '))

    for i in range(1, size_b + 1):
        my_dict['group_b'].append(input(f'{i} word of group B: '))

    for elem in my_dict['group_b']:
        indices = [str(i+1) for i, x in enumerate(my_dict['group_a']) if x == elem]
        if not indices:
            print(-1)
        else:
            print(' '.join(indices))


if __name__ == '__main__':
    main()
