class AANode:
    def __init__(self, key, level=1, left=None, right=None):
        self.key = key
        self.level = level
        self.left = left
        self.right = right


class AATree:
    def __init__(self):
        self.root = None

    def skew(self, node):
        if node is not None and node.left is not None and node.left.level == node.level:
            temp = node.left
            node.left = temp.right
            temp.right = node
            node = temp
        return node

    def split(self, node):
        if node is not None and node.right is not None and node.right.right is not None and node.level == node.right.right.level:
            temp = node.right
            node.right = temp.left
            temp.left = node
            temp.level += 1
            node = temp
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return AANode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        # Perform skew and split to maintain AA-tree properties
        node = self.skew(node)
        node = self.split(node)
        return node

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(f"{node.key} (Level {node.level}) ", end="")
            self.inorder_traversal(node.right)

    def max_node_value(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key

    def min_node_value(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node.key

    def sum_node_values(self):
        node = self.root
        sum = 0
        while node is not None:
            sum += node.key
            node = node.right
        return sum
