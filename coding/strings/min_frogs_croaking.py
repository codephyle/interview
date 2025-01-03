# 1419. Minimum Number of Frogs Croaking

# You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

# Return the minimum number of different frogs to finish all the croaks in the given string.

# A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

# Examples:

# Input: croakOfFrogs = "croakcroak" Output: 1
#     One frog yelling "croak" twice.

# Input: croakOfFrogs = "crcoakroak" Output: 2
#     The minimum number of frogs is two.
#     The first frog could yell "crcoakroak".
#     The second frog could yell later "crcoakroak".


# Input: croakOfFrogs = "croakcrook" Output: -1
#     The given string is an invalid combination of "croak" from different frogs.

def minNumberOfFrogs(croakOfFrogs):
    count = [0] * 5
    frogs = 0
    
    for char in croakOfFrogs:
        if char == "c":
            count[0] += 1
            frogs = max(frogs, count[0])
        elif char == "r":
            count[1] += 1
        elif char == "o":
            count[2] += 1
        elif char == "a":
            count[3] += 1
        elif char == "k":
            count[4] += 1
            for i in range(5):
                count[i] -= 1

        if count[1] > count[0] or count[2] > count[1] or count[3] > count[2] or count[4] > count[3]:
            return -1

    if sum(count) == 0: 
        return frogs
    return -1


croakOfFrogs = "croakcroak"
print(minNumberOfFrogs(croakOfFrogs))
