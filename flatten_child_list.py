"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.helper(head)
        return head

    def helper(self, head):
        prev, curr = None, head
        while curr:
            if curr.child:
                curr_child = curr.child
                flattened_child = self.helper(curr.child)
                curr.child = None
                original_next = curr.next
                if original_next:
                    original_next.prev = flattened_child
                flattened_child.next = original_next
                curr.next, curr_child.prev = curr_child, curr
                prev, curr =  flattened_child, original_next
            else:
                prev, curr = curr, curr.next
        return prev 
