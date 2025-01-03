"""
BACKSPACE STRING COMPARE

Given two strings s and t, return true if they are equal when both are typed 
into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

"""
# https://leetcode.com/problems/backspace-string-compare/
def backspace_compare(s, t):
    def build(s):
        ans = []
        for c in s:
            if c != "#":
                ans.append(c)
            else:
                ans.pop()
        return "".join(ans)

    return build(s) == build(t)


backspace_compare("ab#c", "ad#c")

# Space O(1) algo
def backspace_compare_2(s, t):
    def next_char(s, i):
        cnt = 0
        while i >= 0:
            if s[i] == "#":
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                break

            i = i - 1
        return i

    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0:
        i1 = next_char(s, i)
        j1 = next_char(t, j)

        # reached start of both strings
        if i1 < 0 and j1 < 0:
            return True

        # one of the string is done
        if i1 < 0 or j1 < 0:
            return False

        if s[i1] != s[j1]:
            return False

        i, j = i1 - 1, j1 - 1
    return True


# backspace_compare_2("ab#c", "ad#c")
backspace_compare_2("ab##", "c#d#")
