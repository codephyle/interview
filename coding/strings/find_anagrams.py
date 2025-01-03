# Find all anagrams in a string
#
# Given two strings s and p, return an array of all the start indices
# of p's anagrams in s. You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase, typically
# using all the original letters exactly once.
from collections import Counter


def find_anagrams(s, p):
    result = []
    pc = Counter(p)
    sc = Counter(s[: len(p) - 1])

    j = 0
    for i in range(len(p) - 1, len(s)):
        sc[s[i]] += 1
        if pc == sc:
            result.append(j)
        sc[s[j]] -= 1

        j += 1

    return result


find_anagrams("abab", "ab")
