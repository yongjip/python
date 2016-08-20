class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = heaad

    def append(self, new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, element):
        current = self.head
        found = False
        count = 1
        while current and found is False:
            if current == element:
                return 'position: ' + count
            else:
                count += 1
                current = current.next
        return 'Element not in list'

    def insert(self, new_element, position):
        if self.head is None and position == 1:
            self.head = new_element
        else:
            current = self.head
            previous = None
            count = 1
            while current and count < position:
                count += 1
                previous = current
                current = current.next
            if current != position:
                return "The length of position is longer than the length of list"
            else:
                previous.next = new_element
                new.element.next = current

    def delete(self, value):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current == value:
                found = True
            else:
                previous = current
                current = current.next
        if found is True:
            previous.next = current.next
        return found
