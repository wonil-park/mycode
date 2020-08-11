#!/usr/bin/env python3
icecream = ["flavors", "salty"]

icecream.append(99)

name = input("Please enter your name: ").title()

print(f"{icecream[-1]} {icecream[0]}, and {name} chooses to be {icecream[1]}")
