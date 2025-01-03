# Write a function that takes an unsigned integer and
# returns the number of '1' bits it has (also known as the Hamming weight).

# brute force
def cheat(n):
    return bin(n).count("1")

# straight forward
def count_bits(n):
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1
    return cnt


# Using bit operation to cancel a 1 in each round
# Think of a number in binary
# n     is XXXXXX1000,
# n - 1 is XXXXXX0111.
# n & (n - 1) will be XXXXXX0000 which will just remove the most significant 1
#
# :-) Have a drink
def hamming_weight(n):
    cnt = 0
    while n:
        n = n & n - 1
        cnt += 1
    return cnt


# O(1) 24 arithmetic operations. faster methods exists!
def hamming_weight_1(n):
    n = (n & 0x55555555) + (n >>  1 & 0x55555555); # put count of each  2 bits into those  2 bits 
    n = (n & 0x33333333) + (n >>  2 & 0x33333333); # put count of each  4 bits into those  4 bits 
    n = (n & 0x0F0F0F0F) + (n >>  4 & 0x0F0F0F0F); # put count of each  8 bits into those  8 bits 
    n = (n & 0x00FF00FF) + (n >>  8 & 0x00FF00FF); # put count of each 16 bits into those 16 bits 
    n = (n & 0x0000FFFF) + (n >> 16 & 0x0000FFFF); # put count of each 32 bits into those 32 bits 
    return n

assert cheat(127) == hamming_weight(127)
assert cheat(127) == hamming_weight_1(127)
