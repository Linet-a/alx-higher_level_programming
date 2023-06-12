#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = len(sys.argv) - 1
    arg = "argument" if num_args == 1 else "arguments"
    sep = ":" if num_args > 0 else "."
    print("{}{}{}".format(num, " " + arg if num > 0 else "", sep))
    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
