def get_formatted_name(first: str, last: str, middle='') -> str:
    """Возвращает отформатированное полное имя"""
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'

    return full_name.title()
