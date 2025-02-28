import sys
from typing import NoReturn
from string import punctuation


def text_analyzer(text: str = ...) -> NoReturn:
    """
    This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.

    Args:
        text (str): The text to analyze.
    """

    if text is ...:
        print("MissingError: text argument is missing.")
        return

    if type(text) is not str:
        print(f"TypeError: text argument must be a 'str', not {type(text).__name__}.")
        return

    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    printable_count = 0

    for letter in text:
        if not letter.isprintable():
            continue
        printable_count += 1
        if letter.isupper():
            upper_count += 1
        elif letter.islower():
            lower_count += 1
        elif letter.isspace():
            space_count += 1
        elif letter in punctuation:
            punctuation_count += 1

    print(
        f"The text contains {printable_count} printable character(s):",
        f"- {upper_count} upper letter(s)",
        f"- {lower_count} lower letter(s)",
        f"- {punctuation_count} punctuation mark(s)",
        f"- {space_count} space(s)",
        sep="\n",
    )


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided.")
        quit()

    if len(sys.argv) == 1:
        print("Usage: python count.py STRING")
        quit()

    text_analyzer(sys.argv[1])
