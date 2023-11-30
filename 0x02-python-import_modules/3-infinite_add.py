#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tp = 0
    for x in range(len(sys.argv) - 1):
        tp += int(sys.argv[x + 1])
    print(tp)
