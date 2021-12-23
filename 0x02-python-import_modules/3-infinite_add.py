#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_argv = len(argv)
    suma = 0
    if (len_argv == 1):
        print("{}".format(suma))
    else:
        for i in range(1, len_argv):
            suma += int(argv[i])
        print("{}".format(suma))
