# 1297. Maximum Number of Occurrences of a Substring

# Given a string s, return the maximum number of occurrences of any substring under the following rules:

# The number of unique characters in the substring must be less than or equal to maxLetters.
# The substring size must be between minSize and maxSize inclusive.

# Example 1:

# Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# Output: 2
# Explanation: Substring "aab" has 2 occurrences in the original string.
# It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).


# Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# Output: 2
# Explanation: Substring "aaa" occur 2 times in the string. It can overlap.

# 
# If a string have occurrences x times,
# any of its substring must appear at least x times.

# There must be a substring of length minSize, that has the most occurrences.
# So that we just need to count the occurrences of all substring with length minSize.
# Find the maximum occurrences of all substrings with length k = minSize

def max_occurrences(s, maxLetters, minSize, maxSize):
    substring_counts = {}
    max_occurrences = 0

    for i in range(len(s) - minSize + 1):
        substring = s[i : i + minSize]
        unique_chars = len(set(substring))

        if unique_chars <= maxLetters:
            substring_counts[substring] = substring_counts.get(substring, 0) + 1
            max_occurrences = max(max_occurrences, substring_counts[substring])

    return max_occurrences

