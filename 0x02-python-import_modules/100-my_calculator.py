#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    len_argv = len(argv)
    operator = ['+', '-', '*', '/']
    fun = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
    }
    if (len_argv != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    for i in range(0, len_argv):
        if (operator[i] == op):
            print("{0} {1} {2} = {3}".format(a, op, b, fun[op](a, b)))
            exit(0)
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
