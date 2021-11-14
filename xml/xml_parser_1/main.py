import xml.etree.ElementTree as etree


def get_attr_number(node) -> int:
    """
    Функция получает на вход элемент, который является валидным xml документом.
    Печатает счет этого документа.
    Счет - это общая сумма количество атрибутов каждого элемента.

    :param node:
    :return:
    """

    result = 0
    for elem in node.iter():
        result += len(elem.attrib)
    return result


if __name__ == '__main__':

    # Блок с формированием входных данных из файла
    with open('main.txt', 'r') as f:
        xml = f.read()

    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
