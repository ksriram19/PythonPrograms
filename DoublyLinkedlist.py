
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None



def insertbegin(self,data):
    new_node = Node(data)
    if self.head == None:
        print("Freshnode")
        self.head = new_node

    else:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
def delete(self):
    current = self.head.next
    current.prev = None
    self.head = current

def traverse(self):
    current = self.head
    while current.next != None:
        print(f"{current.data}<->")
        current = current.next
    print(f"None")    


insertbegin(3)
insertbegin(6)
insertbegin(5)
insertbegin(7)

traverse()

delete()
traverse()
