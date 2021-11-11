if __name__ == '__main__':

    def my_decorator(func):
        def inner():
            print('=' * 30)
            func()
            print('+' * 30)
        return inner

    @my_decorator
    def my_func():
        print('Hello world!')

    my_func()
