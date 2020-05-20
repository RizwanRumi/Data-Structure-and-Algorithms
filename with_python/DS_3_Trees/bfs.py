"""
making a tree that we will traverse

Example:    apple
             /\
            /  \
       banana   cherry
          /\
         /  \
      dates  orange
"""


# traverse a tree BFS and Data structure : QUEUE

class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree(object):

    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


tree = Tree("Apple")
tree.get_root().set_left_child(Node("Banana"))
tree.get_root().set_right_child(Node("Cherry"))
tree.get_root().get_left_child().set_left_child(Node("Dates"))
tree.get_root().get_left_child().set_right_child(Node("Orange"))

# queue for bfs
# from collections import deque
# q = deque()
# q.appendleft("apple")
# q.appendleft("banana")
# print(q)
#
# q.pop()
# print(q)

from collections import deque


class Queue(object):

    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


'''
q = Queue()
q.enq("apple")
q.enq("banana")
q.enq("cherry")

print(q)

print(q.deq())

print(q)
'''

'''
visit_order = list()
q = Queue()

# start at the root node and add it to the queue
node = tree.get_root()
q.enq(node)
print(q)

# dequeue the next node in the queue.
# "visit" that node
# also add its children to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f" visit order: {visit_order}")
print(q)

# dequeue the next node (banana)
# visit it, and add its children (dates, orange) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f" visit order: {visit_order}")
print(q)

# dequeue the next node (cherry)
# visit it, and add its children (there are None) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f"visit order: {visit_order}")
print(q)

# dequeue the next node (dates)
# visit it, and add its children (there are None) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f"visit order: {visit_order}")
print(q)

# dequeue the next node (orange)
# visit it, and add its children (there are None) to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())

print(f"visit order: {visit_order}")
print(q)
'''

"""
Queue -> Enqueue: (insert) and Dequeue: (remove)

BFS implementation step:
# queue
# visit order list
# start at root
# add root to queue
# while queue is not empty:
    # dequeue the node
    # visit the node
    # add the left child if exist
    # add the right child if exist
#return the visit order
"""


def bfs(tree):
    q = Queue()
    visit_order = list()
    node = tree.get_root()
    q.enq(node)

    while len(q) > 0:
        node = q.deq()
        visit_order.append(node)

        if node.has_left_child():
            q.enq(node.get_left_child())

        if node.has_right_child():
            q.enq(node.get_right_child())

    return visit_order

visit_list = bfs(tree)

for val in visit_list:
    print(val)