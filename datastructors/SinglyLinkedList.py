# Python implementation of Singly Linked Lists

class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        size = 0
        current = self.head
        while (current != None):
            current = current.get_next()
            size = size + 1
        return size

    def delete(self, value):
        current=self.head
        prev=current
        while (current!=None):
            if current.get_data()==value:
                prev.set_next(current.get_next())
                return None 
            prev=current 
            current=current.get_next() 

    def read(self):
        current = self.head
        while (current != None):
            print(current.get_data())
            current = current.get_next()