"""
LONGEST PEAK

Write a function that takes in an array of integers and returns the length of the longest peak in the array. A peak is defined as adjacent integers in the array that are _strictly_ increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least, 3 integers are required to form a peak.

Sample:
arr = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
answer = 6 [0,10,6,5,-1,-3]
"""
def longestPeak(arr):
     # there is no peak with 2 elements
    if len(arr) < 3:
        return 0

    peaks = []
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            peaks += i,
    
    print(peaks)

    max_peak_len = 0
    for i in peaks:
        peak_len = 1

        j = i
        while j >= 1 and arr[j-1] < arr[j]:
            peak_len += 1
            j -= 1
        
        j = i
        while j < len(arr) -1 and arr[j+1] < arr[j]:
            peak_len += 1
            j += 1
        
        print(peak_len)
        max_peak_len = max(max_peak_len, peak_len)
            
    return max_peak_len

longestPeak([1, 3, 2])

longestPeak([1,2,3,3,4,0,10,6,5,-1,-3,2,3])

# TODO
def longest_peak_eff(arr):
    # do a single pass 
    # whenever you find a peak, expand the peak.
    # update index for next peak find.
    pass