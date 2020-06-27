class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class RingBuffer:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.store = []
        self.cache = []

    def append(self, item):
        if len(self.store) < self.capacity:
            self.store.append(item)

        else:
            self.cache.append(item)
  

    def get(self):
        if len(self.cache) > 0:
            for i in range(len(self.cache)):
                print(self.cache)
            self.cache.extend(self.store[len(self.cache):])
            return self.cache[:self.capacity]
        else: 
            return self.store
