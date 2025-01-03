"""
Dominating XOR

For an array arr of n positive integers, count the unordered pairs (i, j) (0 ≤ i < j < n) where arr[i] XOR arr[j] > arr[i] AND arr[j]. 
XOR denotes the bitwise XOR operation and AND denotes the bitwise AND operation.

Example
Given n = 4, arr  = [4, 3, 5, 2]. All unordered pairs (i, j) are-

    Indices XOR  AND XOR > AND
    (0,1)    7    0    True
    (0,2)    1    4    False
    (0,3)    6    0    True
    (1,2)    6    1    True
    (1,3)    1    2    False
    (2,3)    7    0    True
 

For the first line: 

arr[0] = 4, arr[1] = 3
4 XOR 3 = 7
4 AND 3 = 0
7 > 3
 
There are 4 good pairs where XOR > AND shows True. Return 4.

Function Description
    Complete the function dominatingXorPairs in the editor below.
    dominatingXorPairs has the following parameter:

    int arr[n]:  an array of integers

Returns
    long int: the number of good pairs

Constraints:
    1 ≤ n ≤ 105
    1 ≤ arr[i] < 230

source: HackerRank
"""


def dominatingXorPairs(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] ^ arr[j] > arr[i] & arr[j]:
                cnt += 1

    return cnt


# A pair (i, j) is good if the MSB of both the numbers i,e arr[i] and arr[j] differ.
# This can be seen easily from the bitwise representation of the numbers.
# We can count the numbers with a particular MSB in a hashmap or an array of size 30.
# Then we simply subtract those bad pairs from n * (n - 1) / 2 which have the same MSB.
import math


def dominatingXorPairs(arr):
    n = len(arr)
    msb_count = [0] * 31
    ans = 0
    for i in arr:
        msb = int(math.log(i, 2))
        print(msb)
        ans += sum(msb_count) - msb_count[msb]
        print(ans)
        msb_count[msb] += 1
        print(msb_count)
    return ans


dominatingXorPairs([4, 3, 5, 32, 31])
