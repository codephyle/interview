from collections import Counter

# 767. Reorganize String

# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.

# Example 1:
#     Input: s = "aab" Output: "aba"


# Example 2:
#     Input: s = "aaab" Output: ""

from heapq import heappop, heappush, heapify


def reorganizeString(s):
    ans = []
    # Min heap ordered by character counts, so we will use
    # negative values for count
    pq = [(-count, char) for char, count in Counter(s).items()]
    heapify(pq)

    while pq:
        count_first, char_first = heappop(pq)
        if not ans or char_first != ans[-1]:
            ans.append(char_first)
            if count_first + 1 != 0:
                heappush(pq, (count_first + 1, char_first))
        else:
            if not pq:
                return ""
            count_second, char_second = heappop(pq)
            ans.append(char_second)
            if count_second + 1 != 0:
                heappush(pq, (count_second + 1, char_second))
            heappush(pq, (count_first, char_first))

    return "".join(ans)


def reorganize_string(s):
    # Count the frequency of each character in the string
    freq = Counter(s)

    # Sort the characters based on their frequency in descending order
    sorted_chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

    # Check if the task is impossible
    if freq[sorted_chars[0]] > (len(s) + 1) // 2:
        return ""

    # Create a list to store the rearranged string
    rearranged = [""] * len(s)

    # Start filling the even indexes with the most common characters
    idx = 0
    for char in sorted_chars:
        count = freq[char]
        while count > 0 and idx < len(s):
            rearranged[idx] = char
            count -= 1
            idx += 2

    # Fill the remaining odd indexes with the least common characters
    for char in sorted_chars:
        count = freq[char]
        while count > 0 and idx < len(s):
            if rearranged[idx] == "":
                rearranged[idx] = char
                count -= 1
            idx += 2

    # Convert the list to a string and return the result
    return "".join(rearranged)


# @StefanPochmann
# Put the least common letters at the odd indexes and put the most common letters at the even indexes (both from left to right in order of frequency). The task is only impossible if some letter appears too often, in which case it'll occupy all of the even indexes and at least the last odd index, so I check the last two indexes.


def reorganizeString(self, S):
    a = sorted(sorted(S), key=S.count)
    h = len(a) / 2
    a[1::2], a[::2] = a[:h], a[h:]
    return "".join(a) * (a[-1:] != a[-2:-1])
