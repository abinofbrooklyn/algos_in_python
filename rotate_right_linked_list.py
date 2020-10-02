# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head

        tail = head
        size = 1

        while tail.next != None:
            size += 1
            tail = tail.next

        k %= size
        if k == 0:
            return head

        tail.next = head
        steps_to_rotate = size - k
        rotated_tail = tail
        while steps_to_rotate > 0:
             rotated_tail = rotated_tail.next
             steps_to_rotate -= 1
        rotated_head = rotated_tail.next
        rotated_tail.next = None

        return rotated_head
