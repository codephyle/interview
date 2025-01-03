from collections import OrderedDict

# 146. LRU Cache
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.


# Implement the LRUCache class:
#     LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#     int get(int key) Return the value of the key if the key exists, otherwise return -1.
#     void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#     The functions get and put must each run in O(1) average time complexity.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def remove_last(self):
        if self.head.next == self.tail:
            return None
        last = self.tail.prev
        self.remove(last)
        return last


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.list.remove(node)
            self.list.add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.list.remove(self.cache[key])
        node = Node(key, value)
        self.list.add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.list.remove_last()
            if lru:
                del self.cache[lru.key]
