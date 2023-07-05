#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum_val = 0
            for k in range(len(m_b)):
                sum_val += m_a[i][k] * m_b[k][j]
            row.append(sum_val)
        result.append(row)
    return result
