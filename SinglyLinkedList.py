# Singly Linked list creation

class Node:
    def __init__(self):
        self.data = None
        self.next = None
    
    def setData(self,data):
        self.data = data

    def setNext(self,next):
        self.next = next
    
    def getData(self,data):
        return self.data
    
    def getNext(self,next):
        return self.next

    def hasNext(self):
        return self.next != None
    
    
