class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.value

    def get_right_child(self):
        return self.value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        # return self.left != None
        return self.left is not None

    def has_right_child(self):
        # return self.right != None
        return self.right is not None


class Tree(object):

    def __init__(self, node):
        self.root = node

    # another option for root constructor
    """
    def __init__(self, value):
        self.root = Node(value)
    """

    def get_root(self):
        return self.root


# sample 1
'''
Node0 = Node()
print(f"""
value = {Node0.value}
left = {Node0.left}
right = {Node0.right}
""")

Node0 = Node("Apple")
print(f"""
value = {Node0.value}
left = {Node0.left}
right = {Node0.right}
""")
'''

# sample 2
'''
Node0 = Node("Apple")
Node1 = Node("Banana")
Node2 = Node("Cherry")

Node0.set_left_child(Node1)
Node0.set_right_child(Node2)

print(f"""
node 0 : {Node0.value}
node 0 : Left child : {Node0.left.value}
node 0 : right child : {Node0.right.value}
""")
'''

# sample 3
'''
Node0 = Node("Apple")
Node1 = Node("Banana")
Node2 = Node("Cherry")

print(f"has left child? {Node0.has_left_child()}")
print(f"has right child? {Node0.has_right_child()}")

Node0.set_left_child(Node1)
Node0.set_right_child(Node2)

print(f"has left child? {Node0.has_left_child()}")
print(f"has right child? {Node0.has_right_child()}")

print(f"""
node 0 : {Node0.value}
node 0 : Left child : {Node0.left.value}
node 0 : right child : {Node0.right.value}
""")
'''

# sample 4

Node0 = Node("Apple")
Node1 = Node("Banana")
Node2 = Node("Cherry")

Root = Tree(Node0)

Node0.set_left_child(Node1)
Node0.set_right_child(Node2)

print(f"""
node 0 : {Node0.value}
node 0 : Left child : {Node0.left.value}
node 0 : right child : {Node0.right.value}
""")

