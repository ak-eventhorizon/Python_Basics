import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    """
    Функция получает на вход элемент, который является валидным xml документом.
    Печатает максимальную глубину вложенности тэгов.
    """

    global maxdepth

    if level == maxdepth:
        maxdepth += 1

    for item in elem:
        depth(item, level + 1)


if __name__ == '__main__':

    # Блок с формированием входных данных из файла
    with open('main.txt', 'r') as f:
        xml = f.read()

    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
