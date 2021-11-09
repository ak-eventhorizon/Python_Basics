from html.parser import HTMLParser


def html_parse(s: str) -> None:
    """
    Функция получает на вход строку, которая является фрагментом html-кода.
    И производит парсинг этого кода в части комментариев и данных, в формат:

    >> Single-line Comment
    Comment
    >> Data
    My Data
    >> Multi-line Comment
    Comment_multiline[0]
    Comment_multiline[1]

    Если данные равны '\n' - они не печатаются.

    :param s:
    :return:
    """

    # create a subclass and override the handler methods
    class MyHTMLParser(HTMLParser):

        def handle_comment(self, data):
            if '\n' in data:
                print('>>> Multi-line Comment')
                print(data)
            else:
                print('>>> Single-line Comment')
                print(data)

        def handle_data(self, data):
            if data != '\n':
                print('>>> Data')
                print(data)

    # create the parser and fed it some HTML
    parser = MyHTMLParser()
    parser.feed(s)
    parser.close()


if __name__ == '__main__':

    # # Блок для hackerrank - в гит не помещать
    # test_cases = int(input())
    # content = str()
    #
    # for i in range(test_cases):
    #     if i == test_cases - 1:
    #         content += input()
    #     else:
    #         content += input() + '\n'
    #
    # html_parse(content)

    # Блок с формированием входных данных из файла
    with open('data.txt', 'r') as f:
        content = f.read()

    html_parse(content)
