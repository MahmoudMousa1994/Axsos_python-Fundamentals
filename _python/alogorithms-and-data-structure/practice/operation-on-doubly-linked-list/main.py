class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

#/////////////// Method to add node to the end of the DLL//////////

    def append(self, data): 
        new_node = Node(data)
        if self.head is None: # if the list is empty 
            self.head = new_node
            return
        temp = self.head
        while temp.next: #travers to the last node
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

#///////////////Forward traversal (head to tail)/////////////////

    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp= temp.next
        print("None")

#///////////////Backward traversal (tail to head)/////////////////
    def traverse_backward(self):
        temp = self.head
        if not temp:
            print("List is empty!")
            return
        # move to the tail of the list
        while temp.next:
            temp = temp.next
            # traverse backward from tail to head
        while temp:
            print(temp.data, end="->")
            temp = temp.prev
        print("None")

dll= DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print("Forward Traversal:")
dll.traverse_forward()

print("Backward Traversal:")
dll.traverse_backward()