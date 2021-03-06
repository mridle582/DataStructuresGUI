class MyLinkedList:

    def __init__(self, head):
        self.head = self.tail = self.cursor = head
        self.size = 1

    def add(self, node):
        if self.head is None:
            self.head = self.tail = self.cursor = node
        else:
            self.tail.children[0] = node
            node.parent = self.tail
            self.tail = node
        self.size += 1

    def insert(self, node):
        if self.cursor is None:
            self.head = self.cursor = self.tail = node
        else:
            if self.cursor.children[0] is not None:
                node.children[0] = self.cursor.children[0]
                node.parent = self.cursor
                self.cursor.children[0].parent = node
                self.cursor.children[0] = node
            else:
                self.cursor.children[0] = node
                node.parent = self.cursor
                self.tail = node
        self.size += 1

    def remove(self):
        if self.head is None:
            print('The list is empty.')
        else:
            old_cursor = self.cursor
            if self.size == 1:
                self.head = self.tail = None
            elif self.cursor is self.head:
                self.head = self.head.children[0]
                self.head.parent = None
            elif self.cursor is self.tail:
                self.tail = self.tail.parent
                self.tail.children[0] = None
            else:
                self.cursor.parent.children[0] = self.cursor.children[0]
                self.cursor.children[0].parent = self.cursor.parent
            if self.cursor.children[0] is not None:
                self.cursor = self.cursor.children[0]
            elif self.cursor.parent is not None:
                self.cursor = self.cursor.parent
            else:
                self.cursor = None
            self.size -= 1
            return old_cursor

    def to_string(self):
        output = '['
        cursor = self.head
        while cursor is not None:
            output += cursor.to_string()
            cursor = cursor.children[0]
        return output + ']'


class MyNode:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def __init__(self, data, num_children):
        self.data = data
        self.parent = None
        self.children = [None] * num_children

    def to_string(self):
        return '(' + str(self.data) + ')'
