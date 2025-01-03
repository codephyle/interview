"""
ADD BINARY

Given two binary strings a and b, return their sum as a binary string.

Examples:

    Input: a = "11", b = "1"
    Output: "100"

    Input: a = "1010", b = "1011"
    Output: "10101"

tags: facebook, array, string
"""


def addBinary(a, b):
    carry = 0
    n = max(len(a), len(b))

    a = a.zfill(n)
    b = b.zfill(n)

    print(a, b)
    ans = ""
    m = n - 1
    while m >= 0:
        digit1 = a[m]
        digit2 = b[m]

        sum = 0
        if digit1 == "1" and digit2 == "1":
            if carry:
                sum = 1
            else:
                sum = 0
            carry = 1
        elif digit1 == "0" or digit2 == "0":
            if carry:
                sum = 0
                carry = 1
            else:
                sum = 1
                carry = 0
            print(sum)
        else:
            if carry:
                sum = 1
            else:
                sum = 0
            carry = 0

        ans += str(sum)
        m -= 1

    if carry:
        ans += str(carry)

    return ans[::-1]


addBinary("111", "11")

bin(int("111", 2) + int("11", 2))

# TODO use bitwise operations
# https://leetcode.com/problems/add-binary/solution/
