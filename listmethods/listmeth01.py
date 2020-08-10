#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
print(proto)

protoa = ["ssh", "http", "https"]

proto.append("dns")
protoa.append("dns")

print(proto)

proto2 = [ 22, 80, 443, 53 ]

# Extend() iterates through the arg passed and add each element to the caller 
proto.extend(proto2)
print(proto)

protoa.append(proto2)
print(protoa)

# When reversed
proto.reverse()
protoa.reverse()
print(proto, protoa, sep="\n")

# Stack
last_el = protoa.pop()
print(last_el)
print(protoa)
