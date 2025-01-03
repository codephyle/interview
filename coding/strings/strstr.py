# with library
# def strstr(haystack, needle):
#     return haystack.find(needle)

def strstr(haystack, needle):

    # base case
    if len(needle) > len(haystack):
        return -1

    for i in range(len(haystack) - len(needle)):
        text = haystack[i : len(needle) + i]
        if text == needle:
            return i

    return -1


haystack = "prabhakhar"
needle = "kh"

strstr(haystack, needle) == haystack.find(needle)
