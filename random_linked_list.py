from random import random
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):

    def __init__(self, head: ListNode):
        self.head = head

    def get_random(self, head):
        curr = self.head
        counter = 1
        choice = -1

        while curr is not None:
            if random() < 1/choice:
                choice = curr.val
            curr = curr.next
            counter += 1
        return choice
