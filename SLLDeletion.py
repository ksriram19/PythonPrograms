#Deletion at Begin,End and middle

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def atBegin(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def Delete_at_begin(self):
        if self.head == None:
            print("List empty")
        elif self.head.next == None:
            self.head = None
        else:
            current_node = self.head            # Here we are using a temp variable
            self.head = current_node.next

    def del_at_end(self):
        current = self.head
        while current.next != None:
            previous = current
            current = current.next
        previous.next = None     

    def DeleteMiddle(self,prev_data):
        current = self.head
        while current.next != None and current.data != prev_data:
            previous = current
            current = current.next
        previous.next = current.next   


a = SLL()

a.atBegin(5)
a.atBegin(6)
a.atBegin(7)
a.traverse()

a.del_at_end()
a.traverse()