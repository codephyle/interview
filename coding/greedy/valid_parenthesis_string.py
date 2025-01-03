# 678. Valid Parenthesis String

# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:
#     - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#     - Any right parenthesis ')' must have a corresponding left parenthesis '('.
#     - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#     - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

# Examples:
#     Input: s = "()"  Output: true
#     Input: s = "(*)"  Output: true
#     Input: s = "(*))" Output: true
#     Input: s = "(*)()" 

def checkValidString(s: str) -> bool:
    min_open = 0  # Minimum number of unmatched '('
    max_open = 0  # Maximum number of unmatched '('

    for char in s:
        if char == '(':
            min_open += 1
            max_open += 1
        elif char == ')':
            min_open -= 1
            max_open -= 1
        elif char == '*':
            min_open -= 1  # '*' as ')'
            max_open += 1  # '*' as '('
        
        # If max_open is negative, too many ')' have been encountered
        if max_open < 0:
            return False
        
        # Ensure min_open doesn't drop below 0
        if min_open < 0:
            min_open = 0

    # If min_open is 0, it means all '(' can be matched
    return min_open == 0