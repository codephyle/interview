'''
MOVE ZEROES

Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Examples

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Input: nums = [0]
    Output: [0]
 
Constraints:

    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1
 
**Follow up**: Could you minimize the total number of operations done?

tags: easy, facebook, array
'''
def moveZeroes(nums):
    processed = 0

    # loop and populate the array only non-zero elements
    for i in range(len(nums)):
        if nums[i]:
            nums[processed] = nums[i]
            processed += 1

    # fill the remaining array with zeroes
    for j in range(processed, len(nums)):
        nums[j] = 0

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)

def moveZeroes(nums):
    processed = 0
    # we can simply swap zero and non-zero elements
    # if there are no zeroes, this might swap needlessly
    for i in range(len(nums)):
        if nums[i]:
            nums[i], nums[processed] = nums[processed], nums[i]
            processed += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)