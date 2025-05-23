"""
VALID PALINDROME

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

tags: easy, facebook, string
"""


# https://leetcode.com/problems/valid-palindrome/
def validPalindrome(s):

    def sanitize(s):
        t = ""
        for c in s:
            if c.isalnum():
                t += c.lower()
        return t

    s = sanitize(s)
    l, r = 0, len(s) - 1

    while l <= r:
        # return if chars dont match
        if s[l] != s[r]:
            return False

        l += 1
        r -= 1

    return True


print(validPalindrome("A man, a plan, a canal: Panama"))
