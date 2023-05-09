import sys

import numpy as np


def my_magic_function(x, y):
    return np.log(x) + np.log(y)


def main(argv):
    if len(argv) == 0:
        print("Usage: python core.py number1 [number2 [,,.]]")
        return -1

    magic_result = 0
    for arg in argv:
        value = float(arg)
        magic_result = my_magic_function(magic_result, value)
    print(magic_result)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
