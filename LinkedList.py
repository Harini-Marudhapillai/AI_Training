class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = newNode

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    def delete(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None and temp.next.data != value:
            temp = temp.next

        if temp.next is not None:
            temp.next = temp.next.next

    def search(self, value):
        temp = self.head

        while temp is not None:
            if temp.data == value:
                return True
            temp = temp.next

        return False


list1 = LinkedList()

list1.insertAtEnd(10)
list1.insertAtEnd(20)
list1.insertAtEnd(30)

list1.insertAtBeginning(5)

list1.display()

list1.delete(20)

list1.display()

print(list1.search(30))