def decode_morse(morse_code: str) -> str:
    """
    Decode morse string sequence.

    :param morse_code: string "... --- ..."
    :return:  string "SOS"
    """
    morse = {
        '.-':           'A',
        '-...':         'B',
        '-.-.':         'C',
        '-..':          'D',
        '.':            'E',
        '..-.':         'F',
        '--.':          'G',
        '....':         'H',
        '..':           'I',
        '.---':         'J',
        '-.-':          'K',
        '.-..':         'L',
        '--':           'M',
        '-.':           'N',
        '---':          'O',
        '.--.':         'P',
        '--.-':         'Q',
        '.-.':          'R',
        '...':          'S',
        '-':            'T',
        '..-':          'U',
        '...-':         'V',
        '.--':          'W',
        '-..-':         'X',
        '-.--':         'Y',
        '--..':         'Z',
        '.-.-.-':       '.',
        '--..--':       ',',
        '..--..':       '?',
        '-.-.--':       '!',
        '-..-.':        '/',
        '.--.-.':       '@',
        '.----':        '1',
        '..---':        '2',
        '...--':        '3',
        '....-':        '4',
        '.....':        '5',
        '-....':        '6',
        '--...':        '7',
        '---..':        '8',
        '----.':        '9',
        '-----':        '0',
        '...---...':    'SOS',
    }

    codes = morse_code.split(' ')

    for i in range(len(codes)):
        if codes[i]:
            codes[i] = morse[codes[i]]

    result = '_'.join(codes)
    result = result.replace('___', ' ')
    result = result.replace('_', '')

    return result.strip()
