#!/usr/bin/env python3

hostname = "MTG"

if hostname == "MTG":
    print("The hostname was found to be mtg")

import netifaces
print(netifaces.interfaces())
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    print(netifaces.ifaddresses(i))
