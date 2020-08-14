"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value

   # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the current node's value
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
            # otherwise, it doesn't have a left child
            # we can park the new node here
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal to the current node's value
        else:
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat the process
                self.right.insert(value)
            # otherwise, it doesn't have a right child
            # we can park the new node here
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the Value
    # False if it does not
    def contains(self, target):
        # print(f"does {self.value} equal {target}")
        if target == self.value:
            # print(f"{self.value} does equal {target}")
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            return False

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    # this method doesnt return anything
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)


# def alt_for_each(self, fn):
#     # Depth first Iterative (LIFO)
#     # how do we achieve the same ordering that recursion gave us for free
#     # use a stack to achive the same ordering

#     stack = []
#     stack.append(self)

#     # continue popping from stack as long as there are nodes

#     while len(stack) > 0:
#         current_node = stack.pop()
#         if current_node.right:
#             stack.append(current_node.right)
#         if current_node.left:
#             stack.append(current_node.left)

#     # Breadth first Iterative (FIFO)

#     q = deque()
#     q.append(self)

#     while len(q) > 0:
#         current_node = q.popleft()
#         # check if this node has children(left -> right)
#         if current_node.left:
#             q.append(current_node.left)
#         if current_node.right:
#             q.append(current_node.right)

#         fn(current_node.value)

    # Part 2 -----------------------
# Print all the values in order from low to high
# Hint: Use a recursive, depth first traversal

    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()


# Print the value of every node, starting with the given node,
# in an iterative breadth first traversal

    def bft_print(self):
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            # check if this node has children(left -> right)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)

            print(current_node.value)

# Print the value of every node, starting with the given node,
# in an iterative depth first traversal

    def dft_print(self):
        print(self.value)
        if self.left:
            self.left.dft_print()
        if self.right:
            self.right.dft_print()


# Stretch Goals -------------------------
# Note: Research may be required

# Print Pre-order recursive DFT


    def pre_order_print(self):
        pass

# Print Post-order recursive DFT

    def post_order_print(self):
        pass


# """
# This code is for the Print methods
# """

# bst = BSTNode(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")

# bst.pre_order_print()
# print("in order")
# bst.in_order_print()
# print("post order")
# bst.post_order_print()
