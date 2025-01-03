'''
ROTATE ARRAY BY 'K' ELEMENTS

Write a function that rotates a list by k elements. 
For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. 

Try solving this without creating a copy of the list. How many swap or move operations do you need?

Approach: Do k rotations, one by one. Two many moves. How many?
          For each rotation, we need n moves, so 'kn' moves

          Observe: [1,2,3,4,5,6] -> reverse first k elements [2,1, 3,4,5,6] 
                                 -> reverse last n-k elements [2,1, 6,5,4,3] 
                                 -> reverse the list [3,4,5,6,1,2]
tags: facebook, easy

TODO: try moving elements one time by calculating the final index for a given element
'''
def rotate(arr, k):
    reverse(arr, 0, k-1)
    reverse(arr, k, len(arr)-1)
    reverse(arr, 0, len(arr)-1)
    return arr

def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

assert rotate([1,2,3,4,5, 6], 2) == [3, 4, 5, 6, 1, 2]