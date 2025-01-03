# CAN SUM

# Write a function `canSum(targetSum, numbers)` that takes in a targetSum and an array numbers as arguments.

# The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.

# You may use an element of the array as many times as needed. You may assume that all input numbers are nonnegative.

def canSum(targetSum, nums, memo={}):

    if targetSum in memo:
        return True

    if targetSum == 0:
        return True
    
    if targetSum < 0:
        return False
    
    for num in nums:
        remainder = targetSum - num
        if canSum(remainder, nums, memo):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False

def canSum(targetSum, numbers):
    # Initialize a table of size targetSum + 1 with all False values
    table = [False] * (targetSum + 1)
    
    # Base case: it's always possible to create the sum 0 (by taking no elements)
    table[0] = True
    
    for i in range(targetSum + 1):
        # If the current sum is achievable, proceed to update the table
        if table[i] == True:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = True
    
    return table[targetSum]

# Example usage:
print(canSum(7, [2, 3]))  # Output: True
print(canSum(7, [5, 3, 4, 7]))  # Output: True
print(canSum(7, [2, 4]))  # Output: False
print(canSum(8, [2, 3, 5]))  # Output: True
print(canSum(300, [7, 14]))  # Output: False


