import sys


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: python exec.py STRING...")
        exit()
    print(" ".join(args).swapcase()[::-1])
