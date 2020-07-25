class MyLinkedList:
    
    max_children = 1
    
    def __init__(self, head):
        self.head = self.tail = self.cursor = head
        self.size = 1

    def add(self, node):
        if (self.head is None):
            self.head = self.tail = self.cursor = node
        elif (self.head is not None):
            self.tail.children[0] = node
            node.parent = self.tail
            self.tail = node
        self.size += 1
        
    def insert(self, node, target):
        cursor = self.head
        while cursor is not None and cursor.data != target:
            cursor = cursor.children[0]
        if cursor is None:
            print('The target value does not exist.')
        elif cursor.data == target:
            if cursor.children[0] is not None:
                node.children[0] = cursor.children[0]
                node.parent = cursor
                cursor.children[0].parent = node
                cursor.children[0] = node
            else:
                self.cursor.children[0] = node
                node.parent = self.cursor
                self.tail = node
        size += 1

    def print(self):
        output = '['
        cursor = self.head
        while cursor is not None:
            output += '(' + str(cursor.data)  + ')'
            cursor = cursor.children[0]
        output += ']'
        print(output)


class MyNode:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = [None]

my_list = MyLinkedList(MyNode(5))
my_list.print()
my_list.add(MyNode(4))
my_list.print()
print(my_list.cursor.data)