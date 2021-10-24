import re


def fun(s: str) -> bool:
    if re.match(r'\b[\w_.-]+@[\w_.-]+\.\w{2,3}\b', s):
        return True
    else:
        return False


def filter_mail(emails_list):
    return list(filter(fun, emails_list))


if __name__ == '__main__':
    # n = int(input())
    # emails = list()
    # for i in range(n):
    #     emails.append(input())

    emails = [
        'lara@hackerrank.com',
        'bo@dds#re',
        'brian-23@hackerrank.com',
        ' s ',
        'britts_54@hackerrank.com',
        '44@a..s',
        'nop4$ich@pok.com'
    ]

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
