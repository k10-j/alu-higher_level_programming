#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        end_str = '\n' if i == 8 and j == 9 else ', '
        print("{:02d}, {:02d}".format(i, j), end=end_str)
