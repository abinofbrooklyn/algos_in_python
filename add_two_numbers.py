class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        currentCarry = 0
        head = cur = ListNode(0)

        while l1 or l2 or currentCarry:
            currentVal = currentCarry
            currentVal += 0 if l1 is None else l1.val
            currentVal += 0 if l2 is None else l2.val
            if currentVal >= 10:
                currentCarry = 1
                currentVal -= 10
            else:
                currentCarry = 0

            cur.next = ListNode(currentVal)
            cur = cur.next

            if l1 is None and l2 is None:
                break
            elif l1 is None:
                l2 = l2.next
            elif l2 is None:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next

        return head.next
