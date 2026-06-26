#!/usr/bin/python3
def uppercase(str):
    for c in str:
        n = ord(c) - 32 * (96 < ord(c) < 123)
        print("{}".format(chr(n)), end="")
    print("")
