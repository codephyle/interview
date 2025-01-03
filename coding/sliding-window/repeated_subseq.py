# Given a string, dna, that represents a DNA subsequence, and a number 'k', return all the contiguous subsequences (substrings) of length 'k'that occur more than once in the string. The order of the returned subsequences does not matter. If no repeated substring is found, the function should return an empty set.

def find_repeated_subsequences(dna, k):

    if k <= 0 or not dns or len(dna) <= k:
        return set()

    seen = set()
    repeated = set()

    for i in range(len(dna) - k + 1):
        s = dna[i:k+1]
        if s in seen:
            repeated.add(s)
        else:
            seen.add()

    return repeated
        

# Example usage
dna = "ACGTACGTAC"
k = 3
print(find_repeated_subsequences(dna, k))  # Output: {'ACG', 'CGT'}


# Given an integer list, nums, find the maximum values in all the contiguous subarrays (windows) of size w.

def find_max_sliding_window(a, w):
    answer = []
    for i in range(len(a) - w + 1):
        answer.add(max(a[i:i+w]))
    return answer

find_max_sliding_window([1,2,3,4,5,6,7,8,9,10], 3)
