# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1". Return the number of different expressions that you can build, which evaluates to target.


from typing import List


def findTargetSumWaysBF(nums, target):
    count = 0

    def backtrack(index, curr_sum):
        nonlocal count

        if index == len(nums):
            if curr_sum == target:
                count += 1
            return

        backtrack(index + 1, curr_sum + nums[index])
        backtrack(index + 1, curr_sum - nums[index])

    backtrack(0, 0)
    return count


def findTargetSumWaysRecursive(nums: List[int], target: int):

    total_sum = sum(nums)
    if (total_sum + target) % 2 != 0:
        return 0

    subset_sum = (total_sum + target) // 2
    memo = {}

    def backtrack(index, target):

        if index == len(nums):
            return 1 if target == target else 0

        if (index, target) in memo:
            return memo[(index, target)]

        positive = backtrack(target + nums[index], index + 1)
        negative = backtrack(target - nums[index], index + 1)

        memo[(index, target)] = positive + negative
        return memo[(index, target)]

    return backtrack(0, 0)


def findTargetSumWaysBU(nums, target):
    total_sum = sum(nums)
    if (total_sum + target) % 2 != 0:
        return 0
    subset_sum = (total_sum + target) // 2
    dp = [[0] * (subset_sum + 1) for _ in range(len(nums) + 1)]
    dp[0][0] = 1

    for i in range(1, len(nums) + 1):
        for j in range(subset_sum + 1):

            dp[i][j] = dp[i - 1][j]
            if j >= nums[i - 1]:
                dp[i][j] += dp[i - 1][j - nums[i - 1]]

    return dp[len(nums)][subset_sum]


nums = [1, 1, 1, 1, 1]
target = 1
result = findTargetSumWays(nums, target)
print(result)
