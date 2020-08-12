from MyLinkedList import MyNode


class MyBST:

    def __init__(self, value):
        self.root = MyNode(value, 2)
        self.num_nodes = 1

    def add(self, value):
        self.__add(self.root, None, -1, value)

    def __add(self, root, parent, index, value):
        if root is None:
            root = MyNode(value, 2)
            root.parent = parent
            if parent is not None:
                parent.children[index] = root
            self.num_nodes += 1
            return 'Node added'
        elif root.data == value:
            return 'Value already in tree, no node added.'
        elif value < root.data:
            self.__add(root.children[0], root, 0, value)
        else:
            self.__add(root.children[1], root, 1, value)

    def search(self, value):
        if self.root.data == value:
            return self.root
        else:
            return self.__search(self.root, value)

    def __search(self, root, value):
        if root is None:
            return 'Value is not in tree.'
        if root.data == value:
            return root
        elif root.data < value:
            return self.__search(root.children[1], value)
        else:
            return self.__search(root.children[0], value)

    def remove(self, value):
        root = self.search(value)
        new_root = self.find_new_root(root)

        if new_root is not None:
            if new_root is not root.children[0]:
                new_root.children[0] = root.children[0]
                if root.children[0] is not None:
                    root.children[0].parent = new_root
            if new_root is not root.children[1]:
                new_root.children[1] = root.children[1]
                if root.children[1] is not None:
                    root.children[1].parent = new_root
            if new_root.parent is not None:
                if new_root.parent.children[0] is new_root:
                    new_root.parent.children[0] = None
                else:
                    new_root.parent.children[1] = None
            new_root.parent = root.parent
        if self.root is root:
            self.root = new_root
        else:
            root_index = -1
            if root.parent.children[0] is root:
                root_index = 0
            elif root.parent.children[1] is root:
                root_index = 1
            root.parent.children[root_index] = new_root
        self.num_nodes -= 1
        return root

    def find_new_root(self, root):
        right_subtree = root.children[1]
        left_subtree = root.children[0]
        leftmost_of_right = rightmost_of_left = None
        if right_subtree is not None:
            cursor = right_subtree
            while cursor is not None:
                leftmost_of_right = cursor
                cursor = cursor.children[0]
        if left_subtree is not None:
            cursor = left_subtree
            while cursor is not None:
                rightmost_of_left = cursor
                cursor = cursor.children[1]
        if rightmost_of_left is not None and leftmost_of_right is None:
            return rightmost_of_left
        elif rightmost_of_left is None and leftmost_of_right is not None:
            return leftmost_of_right
        elif rightmost_of_left is not None and leftmost_of_right is not None:
            if root.data - rightmost_of_left.data < leftmost_of_right.data - root.data:
                return rightmost_of_left
            else:
                return leftmost_of_right
        else:
            return None

    def has_children(self, root):
        return root.children[0] is not None or root.children[1] is not None

    def to_string(self):
        if self.root is None:
            return 'The tree is empty.'
        root = self.root.to_string()
        left = self.__to_string(self.root.children[0], 1)
        right = self.__to_string(self.root.children[1], 1)
        if left is None:
            left = ''
        if right is None:
            right = ''
        return root + '\n' + left + right

    def __to_string(self, root, tab_count):
        if root is None:
            return

        left = self.__to_string(root.children[0], tab_count + 1)
        right = self.__to_string(root.children[1], tab_count + 1)

        if left is None:
            left = ''
        if right is None:
            right = ''

        return (tab_count * '    ') + root.to_string() + '\n' + left + right


tree = MyBST(5)
tree.add(3)
tree.add(2)
tree.add(4)
tree.add(7)
print(tree.to_string())
temp = tree.remove(5)
print(temp.to_string())
print(tree.to_string())
temp = tree.remove(4)
print(temp.to_string())
print(tree.to_string())
temp = tree.remove(3)
print(temp.to_string())
print(tree.to_string())

temp = tree.remove(2)
print(temp.to_string())
print(tree.to_string())

temp = tree.remove(7)
print(temp.to_string())
print(tree.to_string())
