# Swapping Nodes in a Linked List
#
# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node
# from the beginning and the kth node from the end (the list is 1-indexed).

# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]

# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1054370/Python-3-or-Swapping-NODES-or-Swapping-Values-or-One-Pass-or-Fully-explained

# Idea
# Find the k-th node from the front.
# Find the k-th last element using two poiners method.
# Swap their values.
# Return the head of the Linked List


def swap_nodes(head, k):

    first = last = head
    for i in range(1, k):
        first = first.next

    null_checker = first
    while null_checker.next:
        last = last.next
        null_checker = null_checker.next

    first.val, last.val = last.val, first.val
    return head
