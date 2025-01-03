# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# naive and brute force
def productExceptSelf(arr):
    products = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i != j:
                product *= arr[j]
        products.append(product)
    return products

# efficient
def productExceptSelf(arr):
    products = [1] * len(arr)

    prefix = 1
    for i in range(len(nums)):
        products[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        products[i] *= postfix
        postfix *= nums[i]
    
    return products
    
 

productExceptSelf([1,2,3,4]) == [24,12,8,6]
productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]