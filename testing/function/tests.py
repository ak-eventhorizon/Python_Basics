import unittest
from main import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Тесты для функций форматирования имени в main.py.

    Методы следует называть test_.... чтобы они запускались
    автоматически при запуске тестового сценария, не нужно опасаться длинных
    имен методов - они должны быть максмально содержательными"""

    def test_first_last_name(self):
        """Имена вида 'John Smith' работают правильно?"""
        formatted_name = get_formatted_name('john', 'smith')
        self.assertEqual(formatted_name, 'John Smith')

    def test_first_middle_last_name(self):
        """Имена вида 'John Robert Smith' работают правильно?"""
        formatted_name = get_formatted_name('john', 'smith', 'robert')
        self.assertEqual(formatted_name, 'John Robert Smith')


if __name__ == '__main__':
    unittest.main()
