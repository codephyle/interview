'''
MERGE TWO SSORTED LISTS

You are given the heads of two sorted linked lists 'list1' and 'list2'.
Merge the two lists in a one sorted list. The list should be made by splicing 
together the nodes of the first two lists.

Return the head of the merged linked list.
    1 -> 2 -> 4
    1 -> 3 -> 4

    1 -> 1 -> 2 -> 3 -> 4 -> 4

tags: facebook, easy, linkedlist
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(l1, l2):
    head = ListNode(0)
    curr = head

    while l1 and l2:
        v1 = l1.val
        v2 = l2.val
        if v1 <= v2:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2
    return head.next



one = ListNode(-1)
dummy = one
for i in range(0, 10, 2):
    one.next = ListNode(i)
    one = one.next
one = dummy.next

two = ListNode(-1)
dummy = two
for i in range(1, 15, 2):
    two.next = ListNode(i)
    two = two.next
two = dummy.next


def printList(l):
    while l:
        print(l.val)
        l = l.next


printList(one)
printList(two)

new = merge(one, two)
printList(new)



