if __name__ == '__main__':

    def my_decorator(func):
        def inner(*args, **kwargs):
            a = func(*args, **kwargs)
            return a + ' DECORATED!'
        return inner

    @my_decorator
    def my_func(message):
        return message

    print(my_func('My message'))
