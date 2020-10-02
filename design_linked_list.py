class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        dummyHead = self.head
        for i in range(index):
            dummyHead = dummyHead.next
        return dummyHead.val

    def addAtHead(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def addAtTail(self, val):
        newNode = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr = newNode
        self.size += 1

    def addAtIndex(self, val, index):
        if index > self.size:
            return

        newNode = Node(val)
        curr = self.head
        if index <= 0:
            newNode.next = curr
            self.head = newNode
        else:
            for i in range(index - 1):
                curr = curr.next
            curr = newNode
        self.size += 1

    def deleteAtIndex(self, val, index):
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
