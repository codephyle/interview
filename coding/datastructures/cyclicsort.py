"""
CYCLIC SORT 

We are given an array containing n objects. Each object, when created, 
was assigned a unique number from the range 1 to n based on their creation sequence. 
This means that the object with sequence number 3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in  O(n) and 
without using any extra space. For simplicity, let’s assume we are passed an integer array 
containing only the sequence numbers, though each number is actually an object.


Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
Example 2:

Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]
Example 3:

Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
"""


def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            t = nums[i]
            nums[i] = nums[nums[i] - 1]
            nums[t - 1] = t
        else:
            i += 1
    return nums


print(cyclic_sort([3, 1, 5, 4, 2]))


# VARIANTS

"""
FIND THE MISSING NUMBER

We are given an array containing n distinct numbers taken from the range 0 to n. 
Since the array has only n numbers out of the total n+1 numbers, find the missing number.

Input: [4, 0, 3, 1]
Output: 2

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""


def find_missing(nums):
    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i]]:
            j = nums[i]
            nums[i], nums[j] = nums[j], nums[i]
            # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]  # Wont work
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)


"""
FIND ALL MISSING NUMBERS 

We are given an unsorted array containing numbers taken from the range 1 to 'n'.
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Input: [2, 4, 1, 2]
Output: 3

Input: [2, 3, 2, 1]
Output: 4

"""


def find_missings(nums):
    pass


"""
FIND THE DUPLICATE NUMBER 

We are given an unsorted array containing 'n+1' numbers taken from the range 1 to 'n'. 
The array has only one duplicate but it can be repeated multiple times. Find that duplicate 
number without using any extra space. You are, however, allowed to modify the input array.

Input: [1, 4, 4, 3, 2]
Output: 4

Input: [2, 1, 3, 3, 5, 4]
Output: 3

Input: [2, 4, 1, 4, 4]
Output: 4

"""


def find_duplicate(nums):
    pass


"""
FIND ALL DUPLICATE NUMBERS

We are given an unsorted array containing n numbers taken from the range 1 to n. 
The array has some numbers appearing twice, find all these duplicate numbers using constant space.

Input: [3, 4, 4, 5, 5]
Output: [4, 5]

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""


def find_all_duplicates(nums):
    pass


"""
FIND THE CORRUPT PAIR

We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'. 
The array originally contained all the numbers from 1 to 'n', but due to a data error, 
one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.


Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
"""


def find_corrupt_pair(nums):
    pass


"""
FIND THE SMALLEST MISSING POSITIVE NUMBER

Given an unsorted array containing numbers, find the smallest missing positive number in it.

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'

Input: [3, -2, 0, 1, 2]
Output: 4

Input: [3, 2, 5, 1]
Output: 4
"""


def find_first_smallest_missing_positive(nums):
    pass


"""
FIND THE FIRST K MISSING POSITIVE NUMBERS

Given an unsorted array containing numbers and a number 'k', 
find the first 'k' missing positive numbers in the array.

Input: [3, -1, 4, 5, 5], k=3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.

Input: [-2, -3, 4], k=2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
"""


