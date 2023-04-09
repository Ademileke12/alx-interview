#!/usr/bin/env python3
import math

def minOperations(n):
    if n <= 1:
        return 0

    # Divide by 2 until n is no longer divisible by 2
    num_divisions = 0
    while n % 2 == 0:
        n //= 2
        num_divisions += 1

    # Check if n is equal to 1
    if n == 1:
        return num_divisions

    # Find prime factors of n
    factors = []
    factor = 2
    while n > 1:
        if n % factor == 0:
            n //= factor
            factors.append(factor)
        else:
            factor += 1

    # Check if we found prime factors
    if not factors:
        return 0

    # Calculate the sum of the factors and return the result
    sum_factors = sum(factors)
    return num_divisions + sum_factors


n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

