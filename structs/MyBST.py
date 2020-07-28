from structs.MyLinkedList import MyNode

class MyBST:

    def __init__(self, value):
        self.root = MyNode(value)
        self.num_nodes = 1

    def add(self, value):
        self.__add(self.root, value)

    def __add(self, root, value):
        if root is None:
            root = MyNode(value)
            self.num_nodes += 1
            return 'Node added'
        elif (value.data == value):
            return 'Value already in tree, no node added.'
        elif (value < root.data):
            self.__add(root.children[0], value)
        else:
            self.__add(root.children[1], value)
