#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    argsLen = len(sys.argv)

    if argsLen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op == "+":
        print(f"{a} {op} {b} = {a + b}")
    elif op == "-":
        print(f"{a} {op} {b} = {a - b}")
    elif op == "*":
        print(f"{a} {op} {b} = {a * b}")
    elif op == "/":
        print(f"{a} {op} {b} = {a / b}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
