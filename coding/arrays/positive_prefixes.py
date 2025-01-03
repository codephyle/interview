# Positive Prefixes

# An array of integers, arr[n], can be rearranged arbitrarily. The prefix sum at index i is defined as psum[i] = arr[0] + arr[1] + ... + arr[i].
# Rearrange the array to maximize the number of positive elements in the psum array. Report the maximum number of positive elements that can be achieved in the array psum.

# Note: Here, a positive value is defined as an integer value greater than 0.

# Example
#     n = 4
#     arr = [-6, 3, 4, -10]
#     One optimal arrangement is [3, 4, -6, -10]. This has an array of prefix sums psum = [3, 7, 1, -9] with 3 positive elements.
#     Return 3, the number of positive elements in psum. There is no way to have more than 3 positive elements.

# Function Description:
#     Complete the function maxPosPrefixes in the editor below.
#     maxPosPrefixes has the following parameter:
#         int arr[n]: an array of integers
# Returns:
#     int: the maximum possible number of positive elements    
# Constraints:
#     1 ≤ n ≤ 10^5
#     -10^9 ≤ arr[i] ≤ 10^9

# source: HackerRank

def maxPosPrefixes(arr):
    
    arr.sort(reverse=True)

    psum, count = 0, 0
    for n in arr:
        psum += n
        if psum > 0:
            count += 1
        else:
            break

    return count