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



import random

class Song:
    def _init_(self,value):
        self.title = value
        self.next = None

class PlayList:
    def _init_(self):
        self.head = None
    
    def addToTal(self,value):
        newNode = Song(value)
        if not self.head:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
    
    def addtoFront(self,value):
        newNode = Song(value)
        newNode.next = self.head
        self.head = newNode
    
    def addAtIndex(self,index,value):
        newNode = Song(value)
        current = self.head
        for i in range(index):
            current = current.next

        newNode.next = current.next
        current.next = newNode

    def play(self):
        current = self.head
        while current:
            print(current.title, end="-->")
            current = current.next
        print("Null")
    
    def getLengthPlayList(self):
        current = self.head
        count = 0
        while current.next:
            count += 1
            current = current.next
        return count
    
    def shuffle(self):
        count = self.getLengthPlayList()
        randInt = random.randint(0,count)
        current = self.head
        for i in range(randInt):
            current = current.next  
        print(current.title)

newList = PlayList()
newList.addToTal("Kiss Me")
newList.addToTal("Dance Off")
newList.addToTal("Real Love")
newList.addToTal("Self Love")
newList.addAtIndex(3,"new")
newList.shuffle()
# newList.play()