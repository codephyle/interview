# Given an array of strings, remove those that are prefixes of one or more of other strings, and return the remaining strings in order as they appear in the input array

# Example:
#   input: ["abc", "ab", "bc", "abc hello"]
#   output: ["bc", "abc hello"]

from collections import defaultdict

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_word = False


    def insert(self, word):
        node = self
        for c in word:
            node = node.children[c]
        node.is_word = True


    def is_prefix(self, word):
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
            if node.is_word and len(node.children) > 0:
                return True
        return False


def remove_prefixes_with_trie(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)

    print(trie.is_prefix("abc hello"))
    result = []
    for string in strings:
        if not trie.is_prefix(string):
            result.append(string)
    return result


# Naive
def remove_prefixes(strings):
    remaining_strings = []
    for i in range(len(strings)):
        is_prefix = False
        for j in range(len(strings)):
            if i != j and strings[i].startswith(strings[j]):
                is_prefix = True
                break
        if not is_prefix:
            remaining_strings.append(strings[i])
    return remaining_strings


print(remove_prefixes_with_trie(["abc", "ab", "abc hello"]))

#   output: ["bc", "abc hello"]
