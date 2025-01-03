# REVERSE A LINKEDLIST
def reverse(head):
    y = head
    p, t = None, None
    while y:
        t = y.next
        y.next = p
        p = y
        y = t
    return p
