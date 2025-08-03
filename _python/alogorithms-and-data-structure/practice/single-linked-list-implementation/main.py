class Node: # A class to represent a single node in the linked list.
    def __init__(self, data):
        self.data = data  # Data to store in the node
        self.next = None # Pointer to the next node

class LinkedList: #A class to represent the single linked list.
    def __init__(self):
        self.head = None # Head of the linked list

    def insert_at_beginning(self, data): # Insert a new node at the beginning of the linked list.
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self

    def insert_at_end(self, data): # Insert a new node at the end of the linked list.
        new_node = Node(data)
        if not self.head: # If the list is empty
            self.head = new_node 
            return
        current = self.head
        while current.next: # Traverse to the end of the list
            current = current.next
        current.next = new_node
        return self
        
    def display(self): # Print the linked list.
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
        return self

linked_list = LinkedList()
linked_list.insert_at_beginning(10).insert_at_beginning(20).insert_at_end(30).display().display()
linked_list.display()





#     def display(self):

# # """Print the linked list."

# current = self.head

# while current:

# print(current.data, end="->")

# current = current.next

# print("None")

# # Example usage

# inked_list = LinkedList()

# inked_list.insert_at_beginning(10)

# inked_list.insert_at_beginning(20)

# inked_list.insert_at_end(30)

# inked_list.display()