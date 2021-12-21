#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)
        if (97 <= num <= 122):
            num = num - 32
        print("{:c}".format(num), end="")
    print("")
    return 0
