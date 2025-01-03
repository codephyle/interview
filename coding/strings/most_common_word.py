"""
18. MOST COMMON WORD

Given a string paragraph and a string array of the banned words banned, 
return the most frequent word that is not banned. It is guaranteed 
there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be 
returned in lowercase.

    Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
    Output: "ball"
    Explanation:
        "hit" occurs 3 times, but it is a banned word.
        "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
        Note that words in the paragraph are not case sensitive,
        that punctuation is ignored (even if adjacent to words, such as "ball,"),
        and that "hit" isn't the answer even though it occurs more because it is banned.

    Input: paragraph = "a.", banned = []
    Output: "a"
"""
from collections import defaultdict


def normalize(s):
    return "".join([c.lower() if c.isalnum() else " " for c in s])


def most_common_word(paragraph, banned):
    banned = set(banned)
    counter = defaultdict(int)

    for word in normalize(paragraph).split():
        if word not in banned:
            counter[word] += 1

    return sorted(counter.items(), key=lambda x: x[1], reverse=True)[0][0]
    # import heapq
    # return heapq.nlargest(1, counter.items(), key=lambda x: x[1])[0][0]


assert (
    most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    == "ball"
)
