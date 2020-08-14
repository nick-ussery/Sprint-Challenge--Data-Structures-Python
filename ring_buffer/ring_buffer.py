class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.contents = []  # list of contents
        self.age = []  # list of contents in the order added

    def append(self, item):

        if len(self.contents) < self.capacity:
            # basic adding of elements before capacity reached
            self.contents.append(item)
            self.age.append(item)
        else:  # if capacity is reached
            old_item_location = self.contents.index(self.age[0])
            self.age.pop(0)
            self.age.append(item)
            self.contents[old_item_location] = item

    def get(self):
        return self.contents
