class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # new_list = LinkedList()
        # current_node = node
        # length = 0
        # while current_node.get_next() != None:
        #     print(f"Current Node: {current_node.get_value()}")
        #     current_node = current_node.get_next()
        #     length += 1
        # new_list.add_to_head(current_node)
        # for i in range(length):
        #     while current_node.next_node != new_list.head or current_node != None:
        #         current_node = current_node.get_next()
        #     new_list.add_to_head(current_node)
        # new_list.add_to_head(prev)
        # return new_list
        if node == None:
            return

        old_next = node.get_next()
        node.set_next(prev)

        if old_next != None:
            self.head = old_next
            self.reverse_list(old_next, node)
