"""
REMOVE K DIGITS FOR SMALLEST NUMBER

Given string 'num' representing a non-negative integer num,
and an integer k, return the smallest possible integer
after removing k digits from num.

hint: next greater element
"""
def remove_k_digits(num, k):
    out = []
    for digit in num:
        while k and out and digit < out[-1]:
            out.pop()
            k -= 1
        out.append(digit)

    if k > 0:
        out = out[:-k]

    return "".join(out).lstrip("0") or "0"


assert remove_k_digits("1432219", 3) == "1219"
assert remove_k_digits("10200", 1) == "200"
assert remove_k_digits("10", 2) == "0"
