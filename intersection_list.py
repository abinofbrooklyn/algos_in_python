class Solution:
    def generateIntersectionNode(self, l1, l2):
        if l1 == None or l2 == None:
            retun None

        l1Length = length(l1)
        l2Length = length(l2)

        if l1Length > l2length:
            l1 = advanceReferenceBy(l1Length - l2Length, l1)
        else:
            l2 = advanceReferenceBy(l2Length - l1Length, l2)

        while l1 != None and l2 != None and l1 != l2:
            l1 = l1.next
            l2 = l2.next
        return l1

    def length(self, head):
        if head == None:
            return 0

        length = 1
        curr = head

        while curr != None:
            length += 1
            curr = curr.next
        return length

    def advanceReferenceBy(self, difference, head):
        while difference > 0:
            head = head.next
            difference -= 1
        return head
