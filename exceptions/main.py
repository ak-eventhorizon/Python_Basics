def int_division(first: str, second: str) -> None:

    try:
        print(int(first) // int(second))
    except ZeroDivisionError as e:
        print('Error code:', e)
    except ValueError as e:
        print('Error code:', e)
    finally:
        print('-----------------------')


if __name__ == '__main__':
    int_division('1', '0')
    int_division('2', '$')
    int_division('3', '1')
