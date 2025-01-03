"""
LETTER COMBINATIONS OF A PHONE NUMBER

Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Examples:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Input: digits = ""
    Output: []

    Input: digits = "2"
    Output: ["a","b", "c"]
"""
# Start with empty string and built it iteratively
def letterCombinations(digits):
    if not digits:
        return []
    
    letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    output = [""]
    for i in range(len(digits)):
        temp = []
        for curr in output:
            for c in letters[int(digits[i]) - 2]:
                temp.append(curr + c)
        output = temp    
    
    return output

letterCombinations("2345")


def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
        return []
    mapping = {'2': ['a','b','c'],
                '3': ['d','e','f'],
                '4': ['g','h','i'],
                '5': ['j','k','l'],
                '6': ['m','n','o'],
                '7': ['p','q','r', 's'],
                '8': ['t','u','v'],
                '9': ['w','x','y', 'z']}
    ans = []
    def dfs(digits, current_path):
        if not digits:
            ans.append(current_path)
        else:
            for letter in mapping[digits[0]]:
                dfs(digits[1:], current_path + letter)
    dfs(digits, "")
    return ans