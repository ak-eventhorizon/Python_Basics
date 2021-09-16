class AnonymousSurvey:
    """Сбор аннонимных ответов на вопросы"""

    def __init__(self, question):
        """Сохранение вопроса и подготовка к сохранению ответов"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Выводит вопрос"""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет один ответ на вопрос"""
        self.responses.append(new_response)

    def show_results(self):
        """Выводит все полученные ответы"""
        print('Survey results:')
        for response in self.responses:
            print(f' - {response}')


if __name__ == '__main__':
    my_survey = AnonymousSurvey('What is your favorite programming language?')

    my_survey.show_question()
    print('(enter "q" at any time to quit)')

    while True:
        answer = input('Language: ')
        if answer == 'q':
            break
        my_survey.store_response(answer)

    print('\nThanks to everyone who answered!')
    my_survey.show_results()
