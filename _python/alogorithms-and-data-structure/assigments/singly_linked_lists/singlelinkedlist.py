class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

# add at front method
    def addFirst(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        print(f"add at first {val}")

# go through the list method
    def print_valuse(self):
        if self.head == None:
            print("The list is empty")
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next

# add at last method
    def addLast(self, val):
        if self.head == None:
            self.addFirst(val)
        
        newNode = Node(val)
        pointer = self.head
        while pointer.next:
            pointer = pointer.next
        pointer.next = newNode
        print(f"add at last {val}")

#  add at palce method
    def addAtPlace(self, val, place):

        if place == 1:
            self.addFirst(val)
            return None
        
        if place == self.getLength() + 1:
            self.addLast(val)
            return None
        
        if place > self.getLength() +1:
            print(f"you skiped the last place by one or more")
            return None
        
        newNode = Node(val)
        pointer = self.head
        for i in range(place -2):
            pointer = pointer.next
        newNode.next = pointer.next
        pointer.next = newNode

# remove the first node
    def removeFirst(self):
        if self.head == None:
            print("The list is empty")
            return None
        removed = self.head
        self.head = self.head.next
        removed.next = None
        print(f"Removed the first node: {removed.data}")


# remove the last node
    def removeLast(self):
        if self.head == None:
            print("the list is empty")
            return None
        
        if self.head.next == None:
            self.removeFirst()
            return None
        pointer = self.head
        while pointer.next.next:
            pointer = pointer.next
        removed = pointer.next
        pointer.next = None
        print(f"Removed the last node: {removed.data}")

# the node length method
    def getLength(self):
        pointer = self.head
        count = 0
        while pointer:
            count += 1
            pointer = pointer.next
        return count

# remove at place method
    def removeAtPlace(self, place):
        if self.head == None:
            print("the list is empty")
            return None
        listLength = self.getLength()
        if place < 1 or place > listLength:
            print("wrong intery")
            return None
        
        if place == 1 :
            self.removeFirst()
            return None
        
        if place == listLength:
            self.removeLast()
            return None
        
        pointer = self.head
        for i in range(place -2):
            pointer = pointer.next
        removed = pointer.next
        pointer.next = pointer.next.next
        print(f"remover node at place:{place}, the removed node is {removed.data}")




sll = SingleLinkedList()
sll.addFirst(3)
sll.addFirst(2)
sll.addFirst(1)
sll.addLast(4)
print(f"dfdf {sll.getLength()}")
sll.addAtPlace(9,6)
sll.print_valuse()



sll.print_valuse()



