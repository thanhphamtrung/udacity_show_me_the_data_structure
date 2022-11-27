class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(new_data)

    def deleteNode(self, delete_value):
        if self.head.value == delete_value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == delete_value:
                node.next = node.next.next
                return
            node = node.next


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.queue = LinkedList()
        self.queueSize = capacity
        self.cache = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            self.queue.deleteNode(key)
            self.queue.push(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.queueSize == 0:
            return      # Edge case
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            self.queue.deleteNode(key)
            self.queue.push(key)
        else:
            # Cache is full
            if self.queueSize == len(self.cache):
                least_key = self.queue.head
                self.queue.deleteNode(least_key)
                self.cache.pop(least_key.value)
            self.queue.push(key)
            self.cache[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5)
our_cache.set(6, 6)
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))
