from datetime import datetime


# декоратор добавляет метку времени к записи в лог
def timed_log(func):
    def inner(*args, **kwargs):
        return f'[{datetime.now()}] {func(*args, **kwargs)}'
    return inner


@timed_log
def log_error(line_number):
    return f'Error in line {line_number}'


@timed_log
def log_done():
    return 'Great! All processed done!'


if __name__ == '__main__':
    print(log_error(57))
    print(log_done())
