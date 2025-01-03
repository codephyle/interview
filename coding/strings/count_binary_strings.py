"""
A binary string is a string consisting only of 0s and 1s. A substring is a contiguous group of characters within a string.
Given a binary string, find the number of substrings that contain an equal number of 0s and 1s and all the 0s and 1s are grouped together. 
Note that duplicate substrings are also counted in the answer. For example, '0011' has two overlapping substrings that meet the criteria: '0011' and '01'.

Example
s = "011001" 
The substrings "01", "10", "1100", and "01" have equal numbers of 0s and 1s with all 0s and 1s grouped consecutively. 
Hence, the answer is 4. Note that the substring "0110" has an equal number of 0s and 1s but is not counted because not all 0s and 1s are grouped together.

Function:
    Complete the function getSubstringCount in the editor below.

    getSubstringCount has the following parameter(s):
        s:  a binary string

Return:
    int: the number of substrings that meet the criteria

Constraints:
1 ≤ length of s ≤ 105
The string s consists of 0s and 1s only.

source: HackerRank
"""

# If there are n ones, followed by m zeros, the number substrings formed would be min(n,m).
# Thus, iterate over the given string and find the number of consecutive occurrences of ones or zeros,
# and then find the sum of minimum of all such alternating occurrences.

def getSubstringCount(s):
    prev, cnt = 0, 1
    ans = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            ans += min(cnt, prev)
            prev = cnt
            cnt = 1
    ans += min(cnt, prev)
    return ans

assert getSubstringCount("001100011") == 6 # "01", "0011", "10", "1100", "01" and "0011" 