"""
INTERSECTION OF TWO ARRAYS

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Examples:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.

Followup:
    Given two integer arrays nums1 and nums2, return an array of their intersection. 
    Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

"""
# https://leetcode.com/explore/interview/card/apple/346/sorting-and-searching/3131/

# O(n+m) Time and O(n) space
def intersection(nums1, nums2):
    
    digits1 = set()
    output = set()

    nums1, nums2 = sorted((nums1, nums2), key=len, reverse=True)
    for n in nums1:
        digits1.add(n)

    for n in nums2:
        if n in digits1:
            output.add(n)

    return list(output)

intersection([1,2,2,1], [2,2])

# O(n log n) | O(1) space 
def intersection(a, b):
    a.sort()
    b.sort()

    ans = set()
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            # if not ans or ans[-1] != a[i]:
            #     ans.append(a[i])
            ans.add(a[i])
            i += 1
            j += 1
    return list(ans)

intersection([4,9,5], [9,4,9,8,4])