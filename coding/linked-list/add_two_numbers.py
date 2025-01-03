'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Examples:

    2->4->3
    5->6->4
    -------
    7->0->8

tags: facebook, linkedlist, easy
'''
# Definition for singly-linked list.
from math import remainder


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    head = ListNode(0)
    curr = head

    carry = 0
    while l1 and l2:
        total = l1.val + l2.val + carry
        carry = 0 # reset carry
        if total >= 10:
            carry = 1
        curr.next = ListNode(total%10)
        curr = curr.next
        l1 = l1.next
        l2 = l2.next

    remainder = l1 or l2
    while remainder:
        total = remainder.val + carry
        carry = 0 # reset carry
        if total >= 10:
            carry = 1
        curr.next = ListNode(total%10)
        curr = curr.next
        remainder = remainder.next

    if carry:
        curr.next = ListNode(carry)
    
    return head.next
