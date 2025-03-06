#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, elem in enumerate(row):
            # Add space after each element except the last one
            end_char = " " if i < len(row) - 1 else ""
            print("{:d}".format(elem), end=end_char)
        print()
