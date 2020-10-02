# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = head
        node_before_reverse_sublist = dummy_head
        pos = 1

        while pos < start:
            node_before_reverse_sublist = node_before_reverse_sublist.next
            pos += 1

        reverse_sublist = node_before_reverse_sublist.next
        while star < end:
            node_to_front = reverse_sublist.next
            reverse_sublist.next = node_to_front.next
            node_to_front.next = node_before_reverse_sublist.next
            node_before_reverse_sublist.next = node_to_front
            start += 1
        return dummy_head.next
