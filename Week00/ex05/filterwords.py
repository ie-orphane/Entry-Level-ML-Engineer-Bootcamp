import sys
from string import punctuation

if __name__ == "__main__":
    if not (
        (len(sys.argv) == 3) and (sys.argv[1].isalpha()) and (sys.argv[2].isnumeric())
    ):
        print("ERROR")
        quit()

    print(
        [
            word
            for word in sys.argv[1].split()
            if len([char for char in word if char not in punctuation])
            > int(sys.argv[2])
        ]
    )
