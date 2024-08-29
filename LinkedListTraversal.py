class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next != None:
            last = last.next
        last.next = new_node


    def listLength(self):
        current = self.head
        count = 0

        while current!= None:
            count = count + 1
            current = current.next
        return count



a = LinkedList()
a.append(8)
a.append(9)
print(a)
b = a.listLength()
print(b)
