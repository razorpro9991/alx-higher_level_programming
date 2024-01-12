#!/usr/bin/python3
# 0-square_matrix_simple.py
# Ebenezer Kissiedu <kissieduebenezzer1@gmail.com>


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    return ([list(map(lambda x: x * x, row)) for row in matrix])
