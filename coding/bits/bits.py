"""
SWAP BITS

Swap bits in a given 64-bit integer, on indices i,j
"""
def swap_bits(n, i, j):

    # No need to swap if the bits are same at indices i, j
    if  (n >> i) & 1 == (n >> j) & 1:
        return n

    # We need a mask with only bits set ar position i and j
    mask = (1 << i) | (1 << j)
    return n ^ mask
    
"""
PARITY

Parity of a binary word 'w' is 1 if number of 1s in w is odd, 0 otherwise.
Compute the parity of a given 64-bit word 

Observe parity of (11010111) is same as parity of (1101)^(0111) and recurse
"""
def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


"""
REVERSE NUMBER

Given a number N, return a number with reverse digits.

1234 => 4321
"""
def reverse_digits(n):
    sign = n >= 0
    result, n = 0, abs(n)
    while n:
        result = result*10 + n%10
        n //= 10
    return result if sign else -result
