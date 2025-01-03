# WORD BREAK

# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated sequence of 
# one or more dictionary words. Note that the same word in the 
# dictionary may be reused multiple times in the segmentation.

# Examples
#     Input: s = "leetcode", wordDict = ["leet","code"]
#     Output: true

#     Input: s = "applepenapple", wordDict = ["apple","pen"]
#     Output: true

#     Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#     Output: false
# https://leetcode.com/problems/word-break/
# https://leetcode.com/problems/word-break/solution/

# ok[i] tells whether s[:i] can be built.

def word_break(s, words):
    ok = [True]
    for i in range(1, len(s) + 1):
        ok += (any(ok[j] and s[j:i] in words for j in range(i)),)
    return ok[-1]


from collections import defaultdict
from functools import lru_cache
class Trie:
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(Trie)
    
    def addWord(self, word):
        curr = self
        for char in word:
            curr = curr.children[char]
        curr.isWord = True


def wordBreak(word, wordDict):
    n = len(word)
    trie = Trie()
    for w in wordDict:
        trie.addWord(w)
    
    @lru_cache(None)
    def dp(start):
        if start == n:
            return True
        curr = trie
        for i in range(start+1, n+1):
            char = word[i-1]
            if char not in curr.children:
                break
            curr = curr.children[char]
            if curr.isWord and dp(i):
                return True
        return False

    return dp(0)

    
assert word_break("leetcode", ["leet", "code"]) == True
assert word_break("applepenapple", ["apple", "pen"]) == True
assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False


assert wordBreak("leetcode", ["leet", "code"]) == True
assert wordBreak("applepenapple", ["apple", "pen"]) == True
assert wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False