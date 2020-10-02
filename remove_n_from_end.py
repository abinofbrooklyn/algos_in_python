# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        right = dummyHead.next

        while n > 0:
            right = right.next
            n -= 1
        left = dummyHead
        while right != None:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummyHead.next  
