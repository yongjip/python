class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.next = None

    def append(self, new_element):
        current = self.value
        if current is None:
            current = new_element
        else:
            while current.next:
                current = current.next
            current.next = new_element

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next


class Stack(object):
    def __init__(self, top=None):
        self.top = top
        self.next = None

    def push(self, new_element):
        new_element.next = self.top
        self.top = new_element

    def pop(self):
        popped = self.top
        if self.top is not None:
            self.top = self.top.next
        return popped
