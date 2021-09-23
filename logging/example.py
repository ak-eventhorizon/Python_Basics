# import os
# import platform
import logging

# if platform.platform().startswith('Windows'):
#     log_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
# else:
#     log_file = os.path.join(os.getenv('HOME'), 'test.log')

log_file = 'test.log'

print('Saving log to: ', log_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=log_file,
    filemode='a',
)


def logging_example():
    """
    Примеры использование в коде инструкций для записей сообщений в лог-файл
    """
    logging.debug('Начало программы')
    logging.info('Какие-то действия')
    logging.warning('Программа умирает!')
    logging.critical('ВСЕ СЛОМАЛОСЬ!!!')
    logging.error('Ошибка в выполнении функции NNN')


if __name__ == '__main__':
    logging_example()
