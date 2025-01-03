def lcs(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]

    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n1][n2]


from functools import lru_cache


@lru_cache(maxsize=None)
def lcs2(s1, s2):
    # common subsequence len is 0, if one of the string is empty
    if len(s1) == 0 or len(s2) == 0:
        return 0
    # found a possible sequence as the first chars match
    if s1[0] == s2[0]:
        return 1 + lcs(s1[1:], s2[1:])
    # else, recurse leaving the first char
    return max(lcs(s1, s2[1:]), lcs(s1[1:], s2))


print(lcs("AGGTAB", "GXTXAYB"))
print(lcs2("AGGTAB", "GXTXAYB"))
