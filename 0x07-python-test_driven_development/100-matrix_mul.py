#!/usr/bin/python3
"""Get the product of two matrices together"""


def matrix_mul(m_a, m_b):
    """Each Matrix m_a and m_b is a list of lists.
       Number of columns in m_a has to be equal number of Rows in m_b
    Args:
        m_a (list): Matrix A
        m_b (list): Matrix B
    Returns:
        list: Product of Matrix A and Matrix B
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list of lists")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list of lists")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list")
    elif not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list")

    if not all(isinstance(num, int) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    elif not all(isinstance(num, int) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) == 0 or len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b[0]) == 0 or len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b must have the same number of columns")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise ValueError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    a_col = 0
    for col in m_a[0]:
        a_col += 1
    b_row = 0
    for row in m_b:
        b_row += 1

    if a_col != b_row:
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = []

    for row_a in m_a:
        m_c_row = []
        for col_b in zip(*m_b):
            sum_all = sum(a * b for a, b in zip(row_a, col_b))
            m_c_row.append(sum_all)
        m_c.append(m_c_row)

    return m_c
