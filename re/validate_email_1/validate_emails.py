import re


def fun(s: str) -> bool:
    if re.match(r'\b[\w_.-]+@[\w_.-]+\.\w{2,3}\b', s):
        return True
    else:
        return False


def filter_mail(emails_list):
    return list(filter(fun, emails_list))


if __name__ == '__main__':

    emails = [
        'lara@hackerrank.com',
        'bo@dds#re',
        'brian-23@hackerrank.com',
        ' s ',
        'britts_54@hackerrank.com',
        '44@a..s',
        'nop4$ich@pok.com',
        'its@gmail.com1',
        'mike13445@yahoomail9.server',
        'rase23@ha_ch.com',
        'daniyal@gmail.coma',
        'thatisit@thatisit'
    ]

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
