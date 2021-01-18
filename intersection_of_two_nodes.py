# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()

        for head in (headA, headB):
            while head:
                if head in seen:
                    return head
                seen.add(head)
                head = head.next
