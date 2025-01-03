# GROUP ANAGRAMS

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Examples

#     Input: strs = ["eat","tea","tan","ate","nat","bat"]
#     Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#     Input: strs = [""]
#     Output: [[""]]

#     Input: strs = ["a"]
#     Output: [["a"]]

# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict


def groupAnagrams(strs):
    groups = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)

    return list(groups.values())


from collections import Counter


def groupAnagrams(strs):
    groups = defaultdict(set)
    for s in strs:
        key = [0] * 26
        for c in s:
            key[ord(c) - ord("a")] += 1
        groups[tuple(key)].add(s)
    return list(groups.values())


groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
