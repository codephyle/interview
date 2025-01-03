
# Given two strings, check whether two strings are isomorphic to each other or not.  Two strings are isomorphic if a fixed mapping exists from the characters of one string to the characters of the other string. 
#
# For example, if there are two instances of the character "a"  in the first string, both these instances should be converted to another character (which could also remain the same character if "a" is mapped to itself) in the second string. This converted character should remain the same in both positions of the second string since there is a fixed mapping from the character "a" in the first string to the converted character in the second string.
# 

def isomorphic_strings(s1, s2):
    if len(s1) != len(s2):
        return False

    mapping = {}
    mapped_chars = set()

    for i in range(len(s1)):
        char1 = s1[i]
        char2 = s2[i]

        if char1 in mapping:
            if mapping[char1] != char2:
                return False
        else:
            if char2 in mapped_chars:
                return False
            mapping[char1] = char2
            mapped_chars.add(char2)

    return True
