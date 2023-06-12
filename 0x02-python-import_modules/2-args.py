#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    arg_str = "argument" if num_args == 1 else "arguments"
    separator = ":" if num_args > 0 else "."
    
    print("Number of {}{}{}".format(num_args, " " + arg_str if num_args > 0 else "", separator))
    
    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
