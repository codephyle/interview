# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS

# Given a string s, find the length of the **longest substring** without repeating characters.

# Examples
#     Input: s = "abcabcbb" Output: 3
#     Explanation: The answer is "abc", with the length of 3.

#     Input: s = "bbbbb" Output: 1
#     Explanation: The answer is "b", with the length of 1.

#     Input: s = "pwwkew" Output: 3
#     Explanation: The answer is "wke", with the length of 3.

# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Approach 1: Generate all substrings -> Check for distinct chars in each substring -> Return longest one
# Approach 2: Sliding Window 
#             -> left, right pointers 
#             -> counter-hash to count the chars by moving right pointer
#             -> on seeing a dup char, move left pointer until the dup count becomes zero
#             -> get the length. update max if needed
# Approach 3: Sliding Window (Optimized)
#             -> insight from above algo.
#             -> instead of moving left pointer 

# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution

def lengthOfLongestSubstring(s):
    left = 0
    max_len = 0
    indices = {}
    for right, char in enumerate(s):
        
        # move the left pointer as far as possible
        if char in indices:
            left = max(left, indices[char] + 1)
        
        indices[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("pwwkew")
lengthOfLongestSubstring("")


# Little optimization - maxlen updated only if left pointer is updated
def lengthOfLongestSubstring(self, s: str) -> int:
    indices = {}
    left, maxlen = 0, 0
    for right, c in enumerate(s):
        if c in indices and left <= indices[c]:
                left = indices[c] + 1
        else:
            maxlen = max(maxlen, right - left + 1)
        indices[c] = right
    return maxlen