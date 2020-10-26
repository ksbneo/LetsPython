import sys
import re


def convert(number):
    print("decimal system: ", number)
    print("binary system: ", bin(number))
    print("octonary system: ", oct(number))
    print("hexadecimal system: ", hex(number))


if __name__ == "__main__":
    if len(sys.argv) >= 2 and bool(re.match('^[0-9]+$', sys.argv[1])) and int(sys.argv[1]) > 100:
        convert(int(sys.argv[1]))
    else:
        print(
            "please input the number, the number should be integer and greater than 100, and try again, e.g. python 1024.py <number>")
