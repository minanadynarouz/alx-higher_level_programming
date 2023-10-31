#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 and num % 5:
            print("FizzBuzz", end=" ")
        elif num % 3:
            print("Fizz", end=" ")
        elif num % 5:
            print("Buzz", end=" ")
        else:
            print(num, end=" " if num != 100 else "\n")
