"""
371. Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.


# Test cases
print(getSum(1, 2))  # Output: 3
print(getSum(2, 3))  # Output: 5

Example 1:

    Input: a = 1, b = 2
    Output: 3

Example 2:

    Input: a = 2, b = 3
    Output: 5
"""


def getSum(a, b):
    # Use bitwise operations to add the two integers
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
