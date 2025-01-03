# Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.
#
# OR
#
# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order among all possible results.


def smallest_subsequence(s):
    last_occurrence = {char: i for i, char in enumerate(s)}
    stack = []
    visited = set()

    for i, char in enumerate(s):
        if char in visited:
            continue
        while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
            visited.remove(stack.pop())
        stack.append(char)
        visited.add(char)

    return ''.join(stack)

# Example usage:

s = "bcabc"
print(smallest_subsequence(s))  # Output: "abc"

