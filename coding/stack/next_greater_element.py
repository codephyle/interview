# Next Greater Element

# The next greater element of some element 'x' in an array is the first greater element that is to the right of 'x' in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2. For each '0 <= i < nums1.length', find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.

# If there is no next greater element, then the answer for this query is -1.

# Return an array 'ans' of length nums1.length such that ans[i] is the next greater element as described above.

def nextGreaterElement(nums1, nums2):

    stack, greaters = [], {}
    for num in nums2:
        while stack and stack[-1] < num:
            greaters[stack.pop()] = num
        stack.append(num)

    ans = []
    for num in nums1:
        ans.append(greaters.get(num, -1))

    print(ans)
    return ans


# test cases
assert nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
assert nextGreaterElement([4, 1, 2], [1, 5, 4, 2]) == [-1, 5, -1]
