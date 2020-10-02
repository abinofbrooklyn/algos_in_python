class Solution:
    def oddEvenList(self, head):
        if head == None or head.next == None:
            return head

        even = head
        odd = head.next
        odd_head = odd

        while odd != None and odd.next != None:
            even.next = odd.next
            even = odd.next
            odd.next = even.next
            odd = even.next
        even.next = odd_head
        return head
