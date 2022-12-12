class Node:
    def __init__(self,key=None,val=None,nxt=None,prev=None):
            self.key = key
            self.val = val
            self.nxt = nxt
            self.prev = prev

class LL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def find(self,key):
        cur = self.head.nxt

        while cur != self.tail:
            if cur.key == key: return cur
            cur = cur.nxt

        return None

    def append(self,key,val):
        new_node = Node(key,val,self.tail,self.tail.prev)
        self.tail.prev.nxt = new_node
        self.tail.prev = new_node
    
    def remove(self,key):
        node = self.find(key)

        if node is not None:
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            return node

        return None

class HashTable:
    def __init__(self):
        self.table_size = 1024
        self.table = [None]*self.table_size
        self.max_load_factor = 0.5
        self.items = 0

    def get_index(self,key,table_size):
        return hash(str(key))%table_size

    def grow(self):
        new_table_size = self.table_size * 2
        new_table = [None]*new_table_size

        for i in range(self.table_size):
            if not self.table[i]: continue
            cur_LL = self.table[i]
            cur = cur_LL.head.nxt

            while cur != cur_LL.tail:
                index = self.get_index(cur.key,new_table_size)
                if not new_table[index]: new_table[index] = LL()
                new_table[index].append(cur.key,cur.val)
                cur = cur.nxt

        self.table = new_table
        self.table_size = new_table_size

    def put(self, key, val):
        if self.items/self.table_size > self.max_load_factor: self.grow()

        index = self.get_index(key,self.table_size)
        if not self.table[index]: self.table[index] = LL()
        
        cur_LL = self.table[index]
        node = cur_LL.find(key)
        
        if node: node.val = val
        else:
            cur_LL.append(key,val)
            self.items += 1

    def get(self, key):
        index = self.get_index(key,self.table_size)
        if not self.table[index]: return -1
        
        node = self.table[index].find(key)
        if node: return node.val
        else: return -1

    def remove(self, key):
        index = self.get_index(key,self.table_size)
        if not self.table[index]: return
        
        node = self.table[index].remove(key)
        if node: self.items -= 1
