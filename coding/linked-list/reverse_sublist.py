# REVERSE A SUB-LIST
#
# Given the head of a LinkedList and two positions ‘p’ and ‘q’,
# reverse the LinkedList from position ‘p’ to ‘q’.

from node import Node


def reverse_sublist(head, start, end):
    if not head:
        return head

    assert start <= end

    dummy = Node(None)
    dummy.next = head

    p = dummy
    for _ in range(1, start):
        p = p.next

    pivot = p.next

    for _ in range(start, end):
        temp = pivot.next
        pivot.next = temp.next
        temp.next = p.next
        p.next = temp

    return dummy.next
