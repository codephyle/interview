# REMOVE KEY

# Remove the specified 'key' from a given array of integers, in place.
# Return the length of the new subarray. The input array may be unordered.

# Input:  [2, 5, 5, 5, 6, 7, 8, 9, 9, 9, 9]
# Output:  6

def remove_key(arr, k):
    i = 0
    for n in arr:
        if n != k:
            a[i] == n
            i += 1
    return i


a = [1, 1, 2, 3, 6, 9, 9, 9, 9]
print(len(a), remove_key(a, 9))
