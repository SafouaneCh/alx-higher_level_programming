#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for ele in matrix:
        if len(ele) == 0:
            print()
        for i in range(len(ele)):
            print("{:d}".format(ele[i]),
                    end="\n" if i is len(ele) - 1 else " ")
