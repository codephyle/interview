# 1290. Convert Binary Number in a Linked List to Integer

# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.

# Example
#     Input: head = [1,0,1] Output: 5
#     Explanation: (101) in base 2 = (5) in base 10

def getDecimalValue(head):
    val = 0
    while head:
        val = 2 * val + head.val
        head = head.next
    return val