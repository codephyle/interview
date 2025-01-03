"""
Quicksort

"""
from random import randint


def partition(arr, low, high):

    # pick a random pivot and swap with first element
    ri = randint(low, high)
    arr[low], arr[ri] = arr[ri], arr[low]

    pivot = arr[low]
    i, j = low, high 

    while True:
        while arr[i] < pivot:
            i += 1
        
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def qsort(arr, low=0, high=None):

    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        qsort(arr, low, pi)
        qsort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
qsort(arr)
print(arr)


def part(nums):

    pivot = nums[0]

    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] <= pivot:
            l += 1
        if nums[r] > pivot:
            r -= 1
        
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    
    
