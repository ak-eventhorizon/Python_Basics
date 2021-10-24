"""
group() - возвращает одну или более совпавших подгрупп
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
m.group(0) - совпадение целиком:
'username@hackerrank.com'
m.group(1) - совпадение по группе в первых скобках
'username'
m.group(2) - совпадение по группе во вторых скобках
'hackerrank'
m.group(1,2,3) - несколько совпадений, возвращаются как кортеж
('username', 'hackerrank', 'com')

groups() - возвращает кортеж, содержащий все группы совпадений
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
m.groups()
('username', 'hackerrank', 'com')

groupdict() - возвращает словарь, содержащий указанные ключи и все совпадения,
проассоциированные этим ключам
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}

"""
import re


def main(s: str) -> None:
    """
    В полученной строке находит первый цифробуквенный символ, идущий подряд более одного раза
    и печатает его
    """
    m = re.search(r'(\w)\1+', s.strip())
    result = m.group(1)
    print(result)


if __name__ == '__main__':
    main(input())
