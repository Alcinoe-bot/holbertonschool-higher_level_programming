#!/usr/bin/python3
if __name__ == "__main__":
    i = 1
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(count))
        while i <= count:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
