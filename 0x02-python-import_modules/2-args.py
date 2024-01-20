#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if len(args) == 1:
        print("{} argument:".format(1))
        print("{}: {}".format((1), args[0]))
    elif len(args) == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(args)))
        for i in range(len(args)):
            print("{}: {}".format((i+1), args[i]))
