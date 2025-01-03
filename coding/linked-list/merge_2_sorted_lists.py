"""
Merge two sorted lists**

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
```
"""

# https://leetcode.com/problems/merge-two-sorted-lists/solution/
def merge_two_lists(l1, l2):

    dummy = Node(-1)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2
    return dummy.next


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def display(self):
        t = self
        while t:
            print(t.val, end=" -> ")
            t = t.next
        print("None")



def merge_two_lists(l1, l2):

    # base condition
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    elif l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2


l1 = Node(0)
l1.next = Node(2)
l1.next.next = Node(4)
l1.next.next.next = Node(6)
l1.next.next.next.next = Node(8)
l1.next.next.next.next.next = Node(10)

l2 = Node(0)
l2.next = Node(2)
l2.next.next = Node(4)
l2.next.next.next = Node(6)
l2.next.next.next.next = Node(8)
l2.next.next.next.next.next = Node(10)

merge_two_lists(l1, l2).display()
