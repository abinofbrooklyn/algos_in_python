class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy_head = ListNode()
        curr = head

        while curr:
            prev = dummy_head
            nxt = dummy_head.next

            while nxt:
                if curr.val < nxt.val:
                    break
                prev = prev.next
                nxt = nxt.next

            tmp = curr.next
            curr.next = nxt
            prev.next = curr

            curr = temp

        return dummy_head.next 
