# Given a string s, return true if the 's' can be palindrome after deleting at most one character from it.

# Example 1:
#     Input: s = "aba"
#     Output: true

# Example 2:
#     Input: s = "abca"
#     Output: true
#     Explanation: You could delete the character 'c'.

# Example 3:
#     Input: s = "abc"
#     Output: false


def valid_palindrome(s):

    def is_palin(s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return is_palin(s, i + 1, j) or is_palin(s, i, j - 1)
        i += 1
        j -= 1
    return True
