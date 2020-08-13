#!/usr/bin/env python3

"""
Author: Wonil
This app assists users to make a decision.
"""
import sys
from os import system
from pynput import keyboard

yes = ["yes", "y", "1"]
no = ["no", "n", "2"]
quit = ['q', '0']
script = "1: yes\t2: no\t0:quit".upper()
conc = "Then don't worry."


def on_press(key):
    try:
        k = key.char
        # if quit.__contains__(k):
        #     sys.exit(0)
    except:
        print('error')


def main():
    """main function"""
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    ans = input_handler("Do you have a problem? ")
    system('clear')
    if ans == "y":
        ans = input_handler("Can you do something about it? ")
        if ans == "y":
            print(conc)


def input_handler(question):
    answered = False
    while not answered:
        print(question, script, sep="\n")
        answer = input().lower()
        system('clear')
        if yes.__contains__(answer):
            return "y"
        elif no.__contains__(answer):
            print(conc)
            answered = True
        elif quit.__contains__(answer):
            sys.exit(0)

main()
