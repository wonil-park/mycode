#!/usr/bin/env python3

"""
Author: Wonil

This app takes user inputs and display them
"""

def main():
    """main function"""
    name = input("What is your name? ").capitalize()
    day_of_the_week = input("What day is today? ").title()
    print(f"Hello, {name}! Happy {day_of_the_week}!")

main()
