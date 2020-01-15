# -*- coding: utf-8 -*-


class Queue:
    def __init__(self):
        self.queue = list()

    def add(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True

        return False

    def remove(self):
        if self.size() > 0:
            return self.queue.pop()

        return 'No elements in Queue!'

    def size(self):
        return len(self.queue)


a_queue = Queue()
a_queue.add('flack')
print(a_queue)

