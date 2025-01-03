# Alien Dictionary

# There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
# You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

# Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

# A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

# Examples

    # Input: words = ["wrt","wrf","er","ett","rftt"]
    # Output: "wertf"

    # Input: words = ["z","x"]
    # Output: "zx"

    # Input: words = ["z","x","z"]
    # Output: ""

# https://leetcode.com/problems/alien-dictionary/

def alienOrder(words):
    # Step 1: Create adjacency list and in-degree dictionary
    adj_list = defaultdict(set)
    in_degree = {}

    for word in words:
        for char in word:
            in_degree[char] = 0

    # Step 2: Build the adjacency list and in-degree dictionary
    for i in range(1, len(words)):
        word1 = words[i - 1]
        word2 = words[i]

        # Check if word2 is a prefix of word1
        if len(word1) > len(word2) and word1.startswith(word2):
            return ""

        for j in range(min(len(word1), len(word2))):
            char1 = word1[j]
            char2 = word2[j]

            if char1 != char2:
                if char2 not in adj_list[char1]:
                    adj_list[char1].add(char2)
                    in_degree[char2] += 1
                break

    # Step 3: Perform topological sorting using Kahn's algorithm
    result = []
    queue = []

    for char in in_degree:
        if in_degree[char] == 0:
            queue.append(char)

    while queue:
        char = queue.pop(0)
        result.append(char)

        for neighbor in adj_list[char]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check if there is a cycle in the graph
    if len(result) != len(in_degree):
        return ""

    return "".join(result)
