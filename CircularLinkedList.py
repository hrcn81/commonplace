'''
Circular Linked List:
'''
class Node:
    def _init_(self, elem):
        self.elem = elem
        self.next = None

class CircularLinkedList:
    def _init_(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def traverse(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.elem, end=' ')
            temp = temp.next
            if temp == self.head:
                break
        print()

    def insert_at_first(self, elem):
        new_node = Node(elem)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def insert_at_last(self, elem):
        new_node = Node(elem)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.tail = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, val):
        if not self.head:
            return False
        if self.head.elem == val:
            if self.head.next == self.head:
                self.head = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            return val
        temp = self.head
        while temp.next != self.head and temp.next.elem != val:
            temp = temp.next
        if temp.next == self.head:
            return False
        temp.next = temp.next.next
        return val

    def print_list(self):
        temp = self.head
        while temp is not None:
            if temp.next is not None:
                print(temp.elem, end=' ----> ')
            else:
                print(temp.nelem,end = ' ')
            temp = temp.next
            if temp == self.head:
                break
        print()


cl1 = CircularLinkedList()

[cl1.insert_at_first(i*10) for i in range(1,11)]
cl1.print_list()

cl1.delete(30)
cl1.print_list()

cl1.delete(20)
cl1.print_list()

cl1.insert_at_last(9000)
cl1.print_list()

cl1.insert_at_first(6000)
cl1.print_list()
