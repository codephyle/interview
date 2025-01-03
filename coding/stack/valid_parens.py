# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
def is_valid(s):
    if not s:
        return True
    stack = []
    closers = {"(": ")", "[": "]", "{": "}"}

    for c in s:
        if s in closers:
            stack.append(c)
        else:
            if not stack or not c != closers[stack.pop()]:
                return False

    return not stack


assert is_valid("(()[{}])") == True
assert is_valid("(]") == False


# Without map


def is_valid2(self, s: str) -> bool:
    stack = []
    for c in s:
        if stack:
            if (
                (c == ")" and stack[-1] == "(")
                or (c == "]" and stack[-1] == "[")
                or (c == "}" and stack[-1] == "{")
            ):
                stack.pop()
                continue
        stack.append(c)
    return not stack
