# First duplicate element in array of len 'n' and containing only elements 1..n, inclusive.

# O(n) time | O(n) space
def firstDuplicate(arr):
    seen = set()
    for n in arr:
        if n in seen:
            return n
        seen.add(n)
    return -1


firstDuplicate([2, 1, 5, 2, 3, 3, 4])


# O(n) time | O(1) space
# but modifies the array. pigeon-hole principle
def firstDuplicate(arr):
    for n in arr:
        index = abs(n)
        if arr[index - 1] < 0:
            return index
        arr[index - 1] *= -1
        print(arr)
    return -1


firstDuplicate([1, 2, 1, 5, 2, 3, 3, 4])
