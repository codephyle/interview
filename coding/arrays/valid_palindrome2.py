'''
VALID PALINDROME II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Examples
    Input: s = "aba"
    Output: true

    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.

    Input: s = "abc"
    Output: false

tags: easy, facebook, string
'''
# https://leetcode.com/problems/valid-palindrome-ii/
def validPalindrome(s):
    l, r = 0, len(s) - 1
    while l <= r:
        
        if r - l == 1 or r - l == 0:
            return True
        
        if s[l] != s[r]:
            if l < len(s)-1 and s[l+1] == s[r]:
                l += 2
                r -= 1
            elif r >= 1 and s[l] == s[r-1]:
                l += 1
                r -= 2
            else:
                return False

        else:
            l += 1
            r -= 1
        
    return True


        