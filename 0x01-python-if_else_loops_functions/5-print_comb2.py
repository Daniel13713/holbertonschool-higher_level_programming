#!/usr/bin/python3
for i in range(0, 100):
    print("{0}{1}".format(i // 10, i % 10), end="")
    if i != 99:
        print(", ", end="")
