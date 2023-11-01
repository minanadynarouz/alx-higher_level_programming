#!/usr/bin/python3
i = 0
x = 1
for num in range(122, 96, -1):
    print("{}".format(chr(num - i)), end="")
    x += 1;
    if (x % 2) == 0:
        i = 32
    else:
        i = 0
