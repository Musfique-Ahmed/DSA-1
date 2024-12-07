class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def addAtBegin(self, data):
        new_item = Node(data)
        if self.head is not None:
            self.head.prev = new_item
            new_item.next = self.head
        self.head = new_item
    
    def addAtEnd(self, data):
        new_item = Node(data)
        if self.head is not None:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = new_item
            new_item.prev = current
        else:
            self.head = new_item

    def addAtMiddle(self, data, key):
        current = self.head
        while (current.data != key) and (current != None):
            current = current.next
        if current is not None:
            new_item = Node(data)
            current.next.prev = new_item
            new_item.next = current.next
            new_item.prev = current
            current.next = new_item
        else:
            print("Number is not found")


    def deleteFirstNode(self):
        if self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            print("The list is empty")







    # def delete_first(self):
    #     if self.head==None:
    #         print("list is empty")
    #     elif self.head.next==None:
    #         self.head=None
    #     else:
    #         self.head=self.head.next
    #         self.head.prev=None

    # def delete_last(self):
    #     if self.head==None:
    #         print("list is empty")
    #     elif self.head.next==None:
    #         self.head=None
    #     else:
    #         current=self.head
    #         while current.next.next:
    #             current=current.next
    #         current.next=None 
        


