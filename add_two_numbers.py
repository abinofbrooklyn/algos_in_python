class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr1 = l1
        ptr2 = l2
        dummyHead = ListNode(0)
        newListPtr = dummyHead
        carry = 0

        while ptr1 != None or ptr2 != None:
            first = ptr1.val if (ptr1 != None) else 0
            second = ptr2.val if (ptr2 != None) else 0
            sum = carry + first + second
            carry = sum // 10
            newListPtr.next = ListNode(sum % 10)
            if ptr1 != None:
                ptr1 = ptr1.next
            if ptr2 != None:
                ptr2 = ptr2.next
            newListPtr = newListPtr.next

        if carry > 0:
            newListPtr.next = ListNode(carry)

        return dummyHead.next
