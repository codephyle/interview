# 387. First Unique Character in a String
#
# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.

# Examples:
#     Input: s = "leetcode"  Output: 0
#     Input: s = "loveleetcode"  Output: 2
#     Input: s = "aabb"  Output: -1

# Constraints:
#     1 <= s.length <= 105
#     s consists of only lowercase English letters.

# https://leetcode.com/problems/first-unique-character-in-a-string/description/

from collections import Counter


def firstUniqChar(s):
    freq = Counter(s)
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1
