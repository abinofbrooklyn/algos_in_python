def reverseList(self, head: ListNode) -> ListNode:
    previous, current = None, head
    while current:
        current.next, previous, current = previous, current, current.next
    return previous
