import sys

def my_magic_function(x, y):
    return x + y

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
    exit(main(sys.argv[1:]))
