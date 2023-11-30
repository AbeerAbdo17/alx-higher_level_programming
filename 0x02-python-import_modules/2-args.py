#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tp = len(sys.argv) - 1
    if tp == 0:
        print("0 arguments.")
    elif tp == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(tp))
    for x in range(tp):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
