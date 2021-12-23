#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    data = dir(hidden_4)
    for i in range(0, len(data)):
        if (data[i][0] != "_" and data[i][1] != "_"):
            print("{}".format(data[i]))
