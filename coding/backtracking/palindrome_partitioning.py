# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aabb"   Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"   Output: [["a"]]


def palindrome_partition(s):
    result = []
    backtrack(s, [], result)
    return result


def backtrack(s, path, result):

    if not s:
        result.append(path)
        return

    for i in range(1, len(s) + 1):
        if is_palindrome(s[:i]):
            backtrack(s[i:], path + [s[:i]], result)


def is_palindrome(s):
    return s == s[::-1]


s = "aabb"
print(palindrome_partition(s))
