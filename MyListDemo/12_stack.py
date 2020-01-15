# -*- coding: utf-8 -*-


class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        # if isinstance(data, list) or isinstance(data, tuple):

        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def peek(self):
        return self.stack[0]

    def remove(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop()


a_stack = Stack()
a_stack.add('a')
print(a_stack, a_stack.peek())
