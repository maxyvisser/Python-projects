#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 08:37:19 2022

@author: maxy
"""

from time import time

while True:
    inp = input("Please enter an exponent: ")

    try:
        exp = int(inp)
    except ValueError:
        print("That's not a number. Try again.")
    except:
        print("Something went wrong, please try again.")

    num2 = 16

    num = 2 ** exp
    print(num)
    print(num2)

    totalstart = time()

    start = time()
    for i in range(num):
        i += num2
    end = time()
    print(f"Finished addition in {end - start} seconds.")

    start = time()
    for i in range(num):
        i -= num2
    end = time()
    print(f"Finished substraction in {end - start} seconds.")

    start = time()
    for i in range(num):
        i *= num2
    end = time()
    print(f"Finished multiplication in {end - start} seconds.")

    start = time()
    for i in range(num):
        i /= num2
    end = time()
    print(f"Finished division in {end - start} seconds.")

    start = time()
    for i in range(num):
        i = i ** num2
    end = time()
    print(f"Finished exponentation in {end - start} seconds.")

    start = time()
    for i in range(num):
        i = i ** (1 / num2)
    end = time()
    print(f"Finished rooting in {end - start} seconds.")

    totalend = time()
    print(f"Program finished in {totalend - totalstart} seconds.")
    input("Press ENTER to try again.")
