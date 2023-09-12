#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Representation of a Pascal's Triangle of n size.

    It returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    all_triangles = [[1]]
    while len(all_triangles) != n:
        triangle = all_triangles[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        all_triangles.append(temp)
    return all_triangles
