'''
STRING TO INTEGER (ATOI)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer 
(similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    - Read in and ignore any leading whitespace.
    - Check if the next character (if not already at the end of the string) is '-' or '+'.
      Read this character in if it is either. This determines if the final result is
      negative or positive respectively. Assume the result is positive if neither is present.
    - Read in next the characters until the next non-digit character or the end of the input is reached.
      The rest of the string is ignored.
    - Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
      If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    - If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
      then clamp the integer so that it remains in the range. Specifically, integers less than -231
      should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    - Return the integer as the final result.

Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

'''
#TODO complete
def atoi(s):
    
    sign = 1
    number = 0
    start = 0

    for i, c in enumerate(s):
        if c is ' ':
            continue
        elif c in "-+":
            if c == '-':
                sign = -1
            start = i + 1
            break
    
    print(start)
    for c in s[start:]:
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            number = number * 10 + (ord(c) - ord('0'))
        else:
            break
    
    return number * sign
    
            
        

atoi('-00000019')