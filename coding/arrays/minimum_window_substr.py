'''
MINIMUM WINDOW SUBSTRING

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s 
such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

EXAMPLE:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.

tags: facebook, array, string
'''
# https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python

from collections import defaultdict

def minSubstring(s, t):
    
    if len(s) < len(t):
        return ""
    indices = defaultdict(list)

    min_window = float("-inf")
    for i, c in enumerate(s):
        if c in 'ABC':
            indices[c].append(i)

        if len(indices) == len(t): # we all the characters
            
    print(indices)

    # for each position of A, what is the best position of B and C
    for pos in indices[t[0]]:
        
        
minSubstring("ADOBECODEBANC", "ABC")