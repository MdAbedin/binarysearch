class Node:
    def __init__(self,key=None,val=None,nxt=None,prev=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def pop(self):
        return self.delete(self.tail.prev)

    def delete(self,node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        return node

    def appendleft(self,node):
        node.nxt = self.head.nxt
        node.prev = self.head
        self.head.nxt.prev = node
        self.head.nxt = node
        return node

class LRUCache:
    def __init__(self, capacity):
        self.maps = dict()
        self.dll = DLL()
        self.capacity = capacity

    def get(self, key):
        if key not in self.maps: return -1
        self.dll.appendleft(self.dll.delete(self.maps[key]))
        return self.maps[key].val

    def set(self, key, val):
        if key not in self.maps:
            if len(self.maps) == self.capacity: self.maps.pop(self.dll.pop().key)
            self.maps[key] = self.dll.appendleft(Node(key,val))
        else:
            self.get(key)
            self.maps[key].val = val
