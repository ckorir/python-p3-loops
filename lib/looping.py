#!/usr/bin/env python3

def happy_new_year():

    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):

    square_integers = [int*int for int in int_list]
    return square_integers

def fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)    
