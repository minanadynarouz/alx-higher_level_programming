#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argsLen = len(argv) - 1
    i = 1

    if argsLen <= 1:
        print("0 arguments.")
    else:
        print(f"{argsLen} arguments:")
        for args in range(1, argsLen + 1):
            final = argv[args]
            print(f"{i}: {final}")
            i += 1
