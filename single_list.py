class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, data):
        new_item = Node(data)
        if self.head is None:
            self.head = new_item
            return
        else:
            new_item.next = self.head
            self.head = new_item

    def insertAtEnd(self, data):
        new_item = Node(data)
        if self.head is None:
            self.head = new_item
            return
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = new_item

    def insertAtMiddle(self, data, key):
        current = self.head
        while (current is not None) and (current.data != key):
            current = current.next
        if current != None:
            new_item = Node(data)
            new_item.next = current.next
            current.next = new_item
        else:
            print(f"The value '{key}' was not found!")
    
    def display(self):
        current = self.head
        while(current):
            print(current.data, end=" -> ")
            current = current.next
        print(f"None")

    def insertAfterOddIndex(self, data):
        if self.head is None:
            print("The list is empty. Operation failed!")
        else:
            index_no = 0
            current = self.head
            while (current):
                if (index_no % 2 != 0):
                    new_item = Node(data)
                    new_item.next = current.next
                    current.next = new_item
                    current = new_item.next
                else:
                    current = current.next
                index_no += 1
    
    def deleteFirstNode(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("The list is empty!")

    def deleteLastNode(self):
        if (self.head is not None):
            current = self.head
            while (current.next != None) and (current.next.next != None):
                current = current.next
            current.next = None
        elif (self.head.next is not None):
            self.head = None
        else:
            print("The list is empty or has only one element!")

    def deleteAnyNode(self,value):
        if self.head is not None:
            current = self.head
            while (current.next.data != value):
                current = current.next
            current.next = current.next.next
        else:
            print("The list is empty!")
    


# ["Anik"]
# [10, "Anik"]

list_1 = SingleLinkedList()
list_1.insertAtBegin("Anik")
list_1.insertAtBegin(10)
list_1.display()
list_1.insertAtEnd(113)
list_1.display()
list_1.insertAtMiddle(45, "Anik")
list_1.display()
list_1.insertAfterOddIndex(0)
list_1.display()
list_1.deleteFirstNode()
list_1.display()

list_2 = SingleLinkedList()
list_2.insertAtBegin(9)
list_2.insertAtBegin(19)
list_2.insertAtBegin(29)
list_2.display()
list_2.deleteLastNode()
list_2.display()
list_2.deleteFirstNode()
list_2.display()
list_2.deleteLastNode()
list_2.display()


list_1.deleteAnyNode(45)
list_1.display()
# list_1.deleteAnyNode("Anik")
# list_1.display()
list_1.deleteAnyNode(0)
list_1.display()