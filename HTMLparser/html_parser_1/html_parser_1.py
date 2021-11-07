from html.parser import HTMLParser


def html_parse(s: str) -> None:
    """
    Функция получает на вход строку, которая является фрагментом html-кода.
    И производит парсинг этого кода в формат:

    Start : Tag1
    End   : Tag1
    Start : Tag2
    -> Attribute2[0] > Attribute_value2[0]
    -> Attribute2[1] > Attribute_value2[1]
    -> Attribute2[2] > Attribute_value2[2]
    Start : Tag3
    -> Attribute3[0] > None
    Empty : Tag4
    -> Attribute4[0] > Attribute_value4[0]
    End   : Tag3
    End   : Tag2

    символ -> означает, что тэг содержит атрибут
    символ > означает, что атрибут имеет значение
    если атрибут не имеет значения - выводится > None
    содержимое html коментариев <!-- Comment --> игнорируется

    :param s:
    :return:
    """

    # create a subclass and override the handler methods
    class MyHTMLParser(HTMLParser):

        def handle_starttag(self, tag, attrs):
            print("Start :", tag)
            if attrs:
                for attr in attrs:
                    name = attr[0]
                    value = 'None' if not attr[1] else attr[1]
                    print(f'-> {name} > {value}')

        def handle_endtag(self, tag):
            print("End :", tag)

        def handle_startendtag(self, tag, attrs):
            print("Empty :", tag)

    # create the parser and fed it some HTML
    parser = MyHTMLParser()
    parser.feed(s)
    parser.close()


if __name__ == '__main__':

    # Блок с формированием входных данных из файла
    with open('data.txt', 'r') as f:
        content = f.read()

    html_parse(content)
