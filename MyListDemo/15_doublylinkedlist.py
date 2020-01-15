# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        self.head = new_node

    def insert(self, index, data):
        pass

    def append(self, data):
        pass

    def remove(self, index):
        pass

    def delete(self, index):
        pass

    def clear(self):
        pass

    def size(self):
        pass

    def get_linklist(self):
        pass



