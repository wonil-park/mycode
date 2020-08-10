#!/usr/bin/env python3

# A simple list: flat list
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

# Display a list and its element
print(list1)
print(list1[1])

list2 = ["juniper"]

# Combine list1 and list2 by extending
list1.extend(list2)

print(list1)

list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

# Append list3 to list1
list1.append(list3)

print(list1)
print(list1[4])
print(list1[4][0])

print("\t======================================\t")
animals = ["fox", "fly", "ant", "cod", "cat", "dog", "yak", "cow", "hen", "koi", "hog"]

for animal in animals:
    print(animal.capitalize(), end=" ")
print()
