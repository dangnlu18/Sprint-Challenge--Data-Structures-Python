from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []
        self.q = deque()

    def append(self, item):
        new_node = Node(item)
        if len(self.store) < self.capacity:
            self.store.append(item)
            self.q.append(item)
        else:
            self.q.append(item)
            evict = self.q.popleft()
            index_in_store = self.store.index(evict)
            self.store[index_in_store] = item


    def get(self):
        return self.store
