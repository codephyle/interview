"""
VALIDATE SUBSEQUENCE

Given two non-empty arrays of integers, write a function that determines whether the second array is a 
subsequence of the first one.

"""
def is_valid_subsequence(arr, seq):
    
    if len(seq) > len(arr):
        return False

    i, j = 0, 0
    while i < len(arr) and j < len(seq):
        if arr[i] == seq[j]:
            j += 1
        i += 1
    return j == len(seq)

is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
