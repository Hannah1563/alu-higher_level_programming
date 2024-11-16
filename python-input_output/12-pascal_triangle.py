#!/usr/bin/python3
"""Task 12 class"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s trian.
    Args:
        n (int): The number of rows in the Pascal’s triangle.
    Returns:
        list: A list of lists representing Pascal’s triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # The first row is always [1]

    for i in range(1, n):
        row = [1]  # The first element of each row is always 1
        for j in range(1, i):
            # Each interior element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle
