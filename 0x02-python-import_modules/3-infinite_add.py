#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argsLen = len(argv)
    sum = 0
    i = 0

    if argsLen == 1:
        print("0")
    elif argsLen == 2:
        print(f"{argv[1]}")
    else:
        for num in range(1, argsLen):
            sum += int(argv[num])
        print(sum)
