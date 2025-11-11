# Define a Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a LinkedList Class to manage the list(keeps track of the head
# and provides helper methods)
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Add a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:       # if list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:     # traverse until last node
            current = current.next
        current.next = new_node

    # Print all nodes
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Insert at beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        # If head needs to be removed 
        if current and current.data == key:
            self.head = current.next
            return
        
        # Search for the node to delete
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return # not found
        prev.next = current.next

# Create a Linked List
l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.display()