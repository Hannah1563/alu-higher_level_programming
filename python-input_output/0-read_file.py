#!/usr/bin/python3
"""Read a text file and print it to stdout."""


def read_file(filename=""):
    """Read a text file and print it to stdout."""
    with open(filename, "r") as f:
        print(f.read(), end="")
