"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
"""
from collections import defaultdict

def longest_substring_with_max_k_distinct_chars(s, k):
    freq = defaultdict(int)
    start = 0
    maxlen = 0
    for i, c in enumerate(s):
        freq[c] += 1
        while len(freq) > k:
            freq[s[start]] -= 1
            if freq[s[start]] == 0:
                del freq[s[start]]
            start += 1
        maxlen = max(maxlen, i - start + 1)
    return maxlen


print(longest_substring_with_max_k_distinct_chars("araaci", 2))

"""
Given a string s, return the length of the longest substring that contains at most two distinct characters.

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

"""
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/


longest_substring_with_max_k_distinct_chars(["A", "B", "C", "B", "B", "C"], 2)
