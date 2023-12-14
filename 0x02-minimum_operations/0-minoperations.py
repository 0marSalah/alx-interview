#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ Minimum Operations """
    if n <= 1:
        return 0
    i = 2
    operations = 0
    while i <= n:
        if n % i == 0:
            operations += i
            n = n / i
        else:
            i += 1
    return operations
