class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
        
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    

    # traversing through a list
    def print_valuse(self):
        runner = self.head # pointer to the list's first node
        while (runner != None): # iterating while runner is node and not None
            print(runner.value)
            runner = runner.next


    # traversing through a list and adding a value to the end
    def add_to_back(self, val):
        if self.head == None: # if the list is empty
            self.add_to_front(val) #run the add_to_front method
        # return self
        new_node = SLNode(val) # create a new instance of our node class with the given value
        runner = self.head # set an iterator to start at the front of the list
        while (runner.next != None): # iterator until the iterator soesn't have a neighbor
            runner = runner.next #increment therunner to the next node in the list
        runner.next = new_node #increment the Runner to the next node in the list

        return self


my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_valuse()



# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class SingleList:
#     def __init__(self):
#         self.head = None

#     def insert_first(self, val):
#         new_node = Node(val)
#         new_node.next = self.head
#         self.head = new_node
#         return self
    
#     def print_valuse(self):
#         pointer = self.head
#         while(pointer != None):
#             print(pointer.val)
#             pointer=pointer.next
#         return self

#     def insert_last(self, val):
#         if self.head == None:
#             self.insert_first(val)
#         else:
#             new_node = Node(val)
#             pointer = self.head
#             while(pointer.next!= None):
#                 pointer= pointer.next
#             pointer.next=new_node
#         return self

# mylst = SingleList()
# mylst.insert_first(10).insert_first(15).insert_last(5).print_valuse()