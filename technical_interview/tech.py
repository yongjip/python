import os
from __future__ import division, print_function

try:
    os.chdir("E:/Documents/Python/technical_interview/")
except:
    print "You are not using Windows, right"
    try:
        os.chdir("/media/yongjip/UUI/Python/technical_interview")
    except:
        print "The paths for Windows and Linux both are not correct."

#Linked List
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


# The node

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data        
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def insert(self, data):
        new_node = node(data)
        new_node.next_node = self.head
        self.head = new_node
    def size(self):
        count=0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current == data:
                found = True
            else:
                current = current.next_node
        if current is None:
            raise ValueError("Data not in list")
        else:
            return current
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current == data:
                found = True
            else:
                previous = current
                current = current.next_node
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.next_node
        else:
            previous.next_node = current.next_node