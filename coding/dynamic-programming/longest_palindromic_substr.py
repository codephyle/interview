"""
LONGEST PALINDROMIC SUBSTRING

Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

    Input: s = "cbbd"
    Output: "bb"
"""
# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
def longestPalindromeSubstr(s):
    longest = ""
    for i in range(len(s)):
        long = expandAround(s, i, i)
        if len(long) > len(longest):
            longest = long

        long = expandAround(s, i, i+1)
        if len(long) > len(longest):
            longest = long

    return longest

def expandAround(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r] 

longestPalindromeSubstr("babad") == "bab"    