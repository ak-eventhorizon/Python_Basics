import re
import email.utils


def email_is_valid(s: str) -> bool:
    """
    A valid email address meets the following criteria:

    format: username@domain.extension

    The username starts with an English alphabetical character, and any subsequent characters
    consist of one or more of the following: alphanumeric characters, -,., and _.

    The domain and extension contain only English alphabetical characters.

    The extension is 1, 2, or 3 characters in length.

    :param s:
    :return:
    """

    pattern = r'(^[a-zA-Z][\w\.-]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})'

    if re.match(pattern, s):
        return True
    else:
        return False


if __name__ == '__main__':

    test_cases = int(input())
    results = list()

    for i in range(test_cases):
        user_input = input()
        name = email.utils.parseaddr(user_input)[0]
        mail = email.utils.parseaddr(user_input)[1]

        if email_is_valid(mail):
            results.append(user_input)

    [print(result) for result in results]

    # INPUT:
    # 2
    # DEXTER <dexter@hotmail.com>
    # VIRUS <virus!@variable.:p>

    # OUTPUT:
    # DEXTER <dexter@hotmail.com>
