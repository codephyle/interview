# TOP K FREQUENT WORDS

# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with 
# the same frequency by their lexicographical order.


# Examples:
#     Input: words = ["i","love","leetcode","i","love","coding"], k = 2
#     Output: ["i","love"]
#     Explanation: "i" and "love" are the two most frequent words.
#                  Note that "i" comes before "love" due to a lower alphabetical order.

#     Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
#     Output: ["the","is","sunny","day"]
#     Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

# https://leetcode.com/explore/interview/card/apple/346/sorting-and-searching/3133/
from collections import defaultdict
import heapq


def topKFrequent(words, k):
    freq = defaultdict(int)
    for word in words:
        freq[word] += 1

    heap = []
    for word, count in freq.items():
        heapq.heappush(heap, (-count, word))
        if len(heap) > k:
            heapq.heappop(heap)

    # extract the top k frequent words from the heap
    result = []
    while heap:
        result.append(heapq.heappop(heap)[1])

    # reverse the result to get the words sorted by frequency from highest to lowest
    result.reverse()

    print(result)


topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
