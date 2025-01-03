'''
202. HAPPY NUMBER

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle 
    which does not include 1.

    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Examples:
    Input: n = 19
    Output: true

    Input: n = 2
    Output: false
'''
#https://leetcode.com/problems/happy-number/
def happyNumber(num):

    def next(num):
        nex = 0
        while num:
            num, remain = divmod(num, 10)
            nex += remain ** 2
        return nex

    seen = set()
    while num != 1:
        num = next(num)
        if num in seen:
            return False
        seen.add(num)

    return True

happyNumber(2)

# but note any integer will 32 bit - atmost 10 digits (64 bit - 20) 
# first iteration gets to mzx 10*81 = 810
