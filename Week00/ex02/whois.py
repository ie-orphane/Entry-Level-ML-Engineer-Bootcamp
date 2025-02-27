import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided.")
        quit()

    if len(sys.argv) == 1:
        print("Usage: python whois.py NUMBER")
        quit()

    try:
        number = int(sys.argv[1])
        if number == 0:
            print(f"I'm Zero.")
        elif number % 2 == 0:
            print(f"I'm Even.")
        else:
            print(f"I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer.")
