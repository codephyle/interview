"""
ROTATE LIST

Given the head of a linked list, rotate the list to the right by k places.

https://leetcode.com/problems/rotate-list/
"""


def rotate_right(head, k):

    if not head or not head.next:
        return head

    tail, n = head, 1
    while tail.next:
        tail = tail.next
        n += 1

    k = k % n
    if k == 0:
        return head

    # make the list circular
    tail.next = head

    split = head
    for _ in range(n - k - 1):
        split = split.next
    head = split.next
    split.next = None

    return head
