# At Beginning,At End and After a node insertion

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def atEnd(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            last = self.head
            while last.next != None:
                last = last.next
            last = new_node
    
    def atBegin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def atMiddle(self,data,prev_data):
        new_node = Node(data)
        current_node = self.head
        while current_node != None and current_node.data != prev_data:
            current_node = current_node.next
        
        new_node.next = current_node.next
        current_node.next = new_node

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

a = SLL()
a.atEnd(3)
a.atBegin(5)
a.atBegin(6)
a.atMiddle(8,5)
a.atMiddle(6,5)
a.atMiddle(2,5)

a.traverse()



    
