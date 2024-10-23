#!/usr/bin/python3

for i in range(97, 123):
    if i != 101 and i != 113:  # Skip 'e' (101) and 'q' (113)
        print(chr(i), end="")
