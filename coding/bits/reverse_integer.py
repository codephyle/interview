"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

    Input: x = 123
    Output: 321

Example 2:

    Input: x = -123
    Output: -321

Example 3:

    Input: x = 120
    Output: 21

"""


def reverse(x: int) -> int:
    # Check if the number is negative
    if x < 0:
        sign = -1
        x = abs(x)
    else:
        sign = 1

    # Reverse the digits of the number
    reverse_x = int(str(x)[::-1])

    # Check if the reversed number is within the 32-bit signed integer range
    if reverse_x > 2**31 - 1:
        return 0

    # Apply the sign to the reversed number
    return sign * reverse_x
