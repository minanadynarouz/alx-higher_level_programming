#!/usr/bin/python3

"""Function to print pascal's triangle upto level <n>"""


def pascal_triangle(n):
    """Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        last_tri = triangles[-1]
        tmp = [1]
        for i in range(len(last_tri) - 1):
            tmp.append(last_tri[i] + last_tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
