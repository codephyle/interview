# 432. All O(1) Data Structure

# Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

# Implement the AllOne class:
#     AllOne() Initializes the object of the data structure.
#     inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
#     dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
#     getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
#     getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".

# Note that each function must run in O(1) average time complexity.

# Example:

#     AllOne allOne = new AllOne();
#     allOne.inc("hello");
#     allOne.inc("hello");
#     allOne.getMaxKey(); // return "hello"
#     allOne.getMinKey(); // return "hello"
#     allOne.inc("leet");
#     allOne.getMaxKey(); // return "hello"
#     allOne.getMinKey(); // return "leet"

# tags: hard, map, linkedlist


class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Node(float("-inf"))  # Sentinel node for head
        self.tail = Node(float("inf"))  # Sentinel node for tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_count = {}  # Maps key to its count
        self.count_nodes = {}  # Maps count to its corresponding node

    def _add_node_after(self, new_node, prev_node):
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        if key in self.key_count:
            current_count = self.key_count[key]
            new_count = current_count + 1
            self.key_count[key] = new_count

            current_node = self.count_nodes[current_count]
            current_node.keys.remove(key)

            if new_count not in self.count_nodes:
                new_node = Node(new_count)
                self.count_nodes[new_count] = new_node
                self._add_node_after(new_node, current_node)

            self.count_nodes[new_count].keys.add(key)

            if len(current_node.keys) == 0:
                self._remove_node(current_node)
                del self.count_nodes[current_count]
        else:
            self.key_count[key] = 1
            if 1 not in self.count_nodes:
                new_node = Node(1)
                self.count_nodes[1] = new_node
                self._add_node_after(new_node, self.head)
            self.count_nodes[1].keys.add(key)

    def dec(self, key):
        if key in self.key_count:
            current_count = self.key_count[key]
            new_count = current_count - 1

            current_node = self.count_nodes[current_count]
            current_node.keys.remove(key)

            if new_count > 0:
                self.key_count[key] = new_count

                if new_count not in self.count_nodes:
                    new_node = Node(new_count)
                    self.count_nodes[new_count] = new_node
                    self._add_node_after(new_node, current_node.prev)

                self.count_nodes[new_count].keys.add(key)
            else:
                del self.key_count[key]

            if len(current_node.keys) == 0:
                self._remove_node(current_node)
                del self.count_nodes[current_count]

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
