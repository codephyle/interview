# Linked Link Cycle

# Given the head of a Singly LinkedList,
# write a function to determine if the LinkedList has a cycle in it or not.


def has_cycle(head):
    if not head:
        return False
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


def has_cycle_except(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False


# LinkedList Cycle Length
# Given the head of a Singly LinkedList with a cycle,
# write a function to find length of the cycle.


def cycle_length(head):

    if not head:
        return 0

    f, s = head, head
    while f and f.next and f != s:
        s = s.next
        f = f.next.next

    # now s must point to the start of the cycle
    t = s
    length = 0
    while True:
        t = t.next
        length += 1
        if t == s:
            break
    return length


# Start of LinkedList Cycle
#
# Given the head of a Singly LinkedList that contains a cycle,
# write a function to find the starting node of the cycle.

# find the cycle length
# move ptr1 for 'length' time
# start second ptr2 and move both till they meet.


def find_cycle_start(head):
    length = cycle_length(head)
    p, q = head, head
    while length:
        p = p.next
        length -= 1
    while p != q:
        p, q = p.next, q.next

    return p


# Happy number
def isHappy(n: int) -> bool:
    while n > 4:
        n = sum(int(d) ** 2 for d in str(n))
        print(n)
    return n == 1


def is_happy(n: int) -> bool:
    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit**2
        return total_sum

    slow = n
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return fast == 1


isHappy(145)
