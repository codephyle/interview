#!/bin/env python3

def remove_nth_node_from_end(head, n):
    left = right = head
    
    for _ in range(n): # 0 < n <= N (num of nodes in the list)
        right = right.next

    if not right: # meaning kth node from end
        return head.next
    
    while right.next:
        right = right.next
        left = left.next
    
    left.next = left.next.next
    return head

# Given an array, colors, which contains a combination of the following three elements:
# 0 (representing red)
# 1 (representing white)
# 2 (representing blue)

# Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue.

# we can use bucket sort / count sort. but extra memory is needed.

def dutch_flag(nums):
    l, r = 0, len(nums) - 1
    i = 0

    while i <= r:
        if nums[i] == 0:
            if nums[l] != 0: # avoid swap
                nums[l], nums[i] = nums[i], nums[l]
            l += 1
            i += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1
    return nums
         
dutch_flag([0,1,1,2,0,2,0,2,1,2])


# middle node in a linked list
def middle_node(head):
    
    if not head:
        return None
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def has_loop(head):

    if not head or not head.next:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False


def happy_number(n):

    def total(n):
        sum = 0
        for c in str(n):
            c = int(c)
            sum += c * c
        return sum
    
    slow = n
    fast = total(n)

    while fast != 1:
        slow = total(slow)
        fast = total(total(fast))
        if slow == fast:
            return False
    
    return True


happy_number("28")

# TODO  
def circular_array_loop(nums):
    size = len(nums)

    for i in range(size):
        slow = fast = i
        forward = nums[i] > 0
        
        index = i % size
        slow = nums[index]
        if slow > 0 and direction == 0:
            continue

        fast = nums[nums[index]%size]
        if fast > 0 and direction == 0:
            continue

        if slow == fast:
            return True
        
    return False

print(circular_array_loop([2,1,-1,-2]))