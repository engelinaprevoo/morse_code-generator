"""
    Written by: Caroline Prevoo

    Date start: 2 april 2021

    Goal      : Translate input string to morse code
"""

# International Morse Code
morse_code = {
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
    ' ': '     '
}

in_string = input("Enter a string: ").upper()
morse = ""
for char in in_string:
    if char in morse_code:
        morse += f"{morse_code[char]}  "
    else:
        # char not in morse_code (e.g. ?, á, %, etc.)
        # use #
        morse += f"#"
print(morse)
