'''
Linked List:
'''

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_first(self, elem):
        temp = self.head
        new_Node = Node(elem)
        self.head = new_Node
        self.head.next = temp

    def add(self, elem):
        new_node = Node(elem)
        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def remove_last(self):
        if self.is_empty():
            print("Cannot remove from an empty list.")
            return
        temp = self.head
        if temp.next is None:
            removed_elem = temp.elem
            self.head = None
            print('Removed', removed_elem)
        else:
            while temp.next.next is not None:
                temp = temp.next
            removed_elem = temp.next.elem
            temp.next = None
            print('Removed', removed_elem)

    def middle_insert(self, val, new_elem):
        temp = self.head
        while temp is not None and temp.elem != val:
            temp = temp.next
        if temp is None:
            print(f"Value {val} not found in the list.")
            return
        new_node = Node(new_elem)
        new_node.next = temp.next
        temp.next = new_node
        return new_elem

    def delete_first(self):
        if self.is_empty():
            print("Cannot delete from empty list.")
            return
        removed_elem = self.head.elem
        self.head = self.head.next
        print('Deleted first element', removed_elem)
        return removed_elem

    def delete(self, val):
        if self.is_empty():
            print("Cannot delete from an empty list.")
            return
        if self.head.elem == val:
            removed_elem = self.head.elem
            self.head = self.head.next
            print('Deleted', removed_elem)
            return removed_elem
        temp = self.head
        while temp.next is not None and temp.next.elem != val:
            temp = temp.next
        if temp.next is None:
            print(f"Value {val} not found in the list.")
            return
        removed_elem = temp.next.elem
        temp.next = temp.next.next
        print('Deleted', removed_elem)
        return removed_elem

    def search(self, elem):
        temp = self.head
        while temp is not None:
            if temp.elem == elem:
                return True
            temp = temp.next
        return False

    def ascending_sort(self):
        c = self.count()
        while c > 0:
            temp = self.head
            while temp.next is not None:
                if temp.elem > temp.next.elem:
                    temp.elem, temp.next.elem = temp.next.elem, temp.elem
                temp = temp.next
            c -= 1

    def descending_sort(self):
        c = self.count()
        while c > 0:
            temp = self.head
            while temp.next is not None:
                if temp.elem < temp.next.elem:
                    temp.elem, temp.next.elem = temp.next.elem, temp.elem
                temp = temp.next
            c -= 1

    def count ( self ):
        temp = self.head
        count = 0
        while (temp.next != None):
            count += 1
            temp = temp.next
        return count

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.elem, end=' ----> ')
            temp = temp.next
        print()


ll1 = LinkedList()

[ll1.add( i * 10 ) for i in range(11,21)]
ll1.print_list()

ll1.insert_first(88)
ll1.print_list()

ll1.remove_last()
ll1.print_list()

ll1.middle_insert(130,800)
ll1.print_list()

ll1.delete(130)
ll1.print_list()

ll1.delete_first()
ll1.print_list()
[ll1.add( i * 5 ) for i in range(21,36)]
ll1.search(120)
ll1.print_list()
print(ll1.sorting())
ll1.ascending_sort()
ll1.print_list()
ll1.descending_sort()
ll1.print_list()
