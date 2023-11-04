#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argsLen = len(argv)
    i = 1

    if argsLen == 1:
        print("0 arguments.")
    elif argsLen == 2:
        print("1 argument:")
        print(f"1: {argv[1]}")
    else:
        print(f"{argsLen - 1} arguments:")
        for args in range(1, argsLen):
            final = argv[args]
            print(f"{i}: {final}")
            i += 1
