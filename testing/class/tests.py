import unittest

from main import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey (анонимных опросов) в main.py.

    Методы следует называть test_.... чтобы они запускались
    автоматически при запуске тестового сценария, не нужно опасаться длинных
    имен методов - они должны быть максмально содержательными"""

    def setUp(self):
        """setUp() - специальный метод для модульного тестирования.
        Создает объекты для каждого тестового метода (test_...)

        В данном случае создает опрос и набор ответов для тестовых методов"""

        self.my_survey = AnonymousSurvey('Some question example')
        self.responses = ['Answer1', 'Answer2', 'Answer3']

    def test_store_single_response(self):
        """Проверяет, что один ответ сохраняется правильно."""

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Проверяет, что три ответа сохраняются правильно."""

        for response in self.responses:
            self.my_survey.store_response(response)

        self.assertEqual(self.responses, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
