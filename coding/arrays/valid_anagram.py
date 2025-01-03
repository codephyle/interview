# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Examples:
#     Input: s = "anagram", t = "nagaram"
#     Output: true

#     Input: s = "rat", t = "car"
#     Output: false

from collections import Counter


def isAnagram(s, t):
    # return Counter(s) == Counter(t)
    if len(s) != len(t):
        return False
    