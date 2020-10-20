import sys


def hello(name):
    print("hello " + name)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "please input your name, and try again, e.g. python helloworld.py <your name>")
    else:
        hello(sys.argv[1])
