def zero_sum_subarrays(arr):
    sums = {}
    curr_sum = 0

    res = []
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0:
            print("Subarray found from index 0 to", i)

        if curr_sum in sums:
            for j in sums[curr_sum]:
                print("Subarray found from index", j + 1, "to", i)
        else:
            sums[curr_sum] = []

        sums[curr_sum].append(i)
    return sums


def print_zero_sum_subarrays(arr):
    # Dictionary to store cumulative sums and their corresponding indices
    sums = {}
    curr_sum = 0
    result = []

    # Traverse through the array
    for i in range(len(arr)):
        curr_sum += arr[i]

        # If current sum is zero, print the subarray from start to current index
        if curr_sum == 0:
            result.append((0, i))

        # If the current sum is seen before, there exists a zero-sum subarray
        if curr_sum in sums:
            indices = sums[curr_sum]
            for index in indices:
                result.append((index + 1, i))
            sums[curr_sum].append(i)
        else:
            sums[curr_sum] = [i]

    print(result)
    # Print all zero-sum subarrays
    for start, end in result:
        print("Subarray with zero sum:", arr[start:end+1])

# Example usage:
arr = [4, 2, -3, -1, 0, 4]
zero_sum_subarrays(arr)
print_zero_sum_subarrays(arr)