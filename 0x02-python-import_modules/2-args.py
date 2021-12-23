#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_argv = len(argv)
    if (len_argv == 1):
        print("0 arguments.")
    elif (len_argv == 2):
        print("1 argument:")
    else:
        print("{0} arguments:".format(len_argv - 1))
    for i in range(1, len_argv):
        if (len_argv > 1):
            print("{0}: {1}".format(i, argv[i]))
