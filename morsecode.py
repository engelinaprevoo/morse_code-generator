"""
    Written by: Caroline Prevoo

    Date start: 2 april 2021

    Goal      : Translate input string to morse code
"""

# International Morse Code
MORSE_CODE = {
    'A': '•-',
    'B': '-•••',
    'C': '-•-•',
    'D': '-••',
    'E': '•',
    'F': '••-•',
    'G': '--•',
    'H': '••••',
    'I': '••',
    'J': '•---',
    'K': '-•-',
    'L': '•-••',
    'M': '--',
    'N': '-•',
    'O': '---',
    'P': '•--•',
    'Q': '--•-',
    'R': '•-•',
    'S': '•••',
    'T': '-',
    'U': '••-',
    'V': '•••-',
    'W': '•--',
    'X': '-••-',
    'Y': '-•--',
    'Z': '--••',
    '1': '•-----',
    '2': '••---',
    '3': '•••--',
    '4': '••••-',
    '5': '•••••',
    '6': '-••••',
    '7': '--•••',
    '8': '---••',
    '9': '----•',
    '0': '-----',
    ' ': '<br>'
}

class MorseCode:

    @staticmethod
    def translate(sentence: str):
        morse_out = ""
        for char in sentence.upper():
            if char in MORSE_CODE:
                morse_out += f"{MORSE_CODE[char]}  "
            else:
                # char not in morse_code (e.g. ?, á, %, etc.)
                # use #
                morse_out += f"#"
        return morse_out


def main():
    in_string = input("Enter a string: ").upper()
    morse_out = ""
    for char in in_string:
        if char in MORSE_CODE:
            morse_out += f"{MORSE_CODE[char]} &nbsp;"
        else:
            # char not in morse_code (e.g. ?, á, %, etc.)
            # use #
            morse_out += f"#"
    print(morse_out)


if __name__ == "__main__":
    main()