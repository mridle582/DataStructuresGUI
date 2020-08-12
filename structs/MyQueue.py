from structs.MyLinkedList import *


class MyQueue:

    def __init__(self, node):
        self.queue = MyLinkedList(node)

    def enqueue(self, node):
        self.queue.add(node)

    def dequeue(self):
        return self.queue.remove()

    def to_string(self):
        return self.queue.toString()
