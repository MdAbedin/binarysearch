class Node:
    def __init__(self,val=None,nxt=None,prev=None):
            self.val = val
            self.nxt = nxt
            self.prev = prev

class LL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def find(self,val):
        cur = self.head.nxt

        while cur != self.tail:
            if cur.val == val: return cur
            cur = cur.nxt

        return None

    def append(self,val):
        new_node = Node(val,self.tail,self.tail.prev)
        self.tail.prev.nxt = new_node
        self.tail.prev = new_node
    
    def remove(self,val):
        node = self.find(val)

        if node is not None:
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            return node

        return None

class CustomSet:
    def __init__(self):
        self.table_size = 1024
        self.table = [None]*self.table_size
        self.max_load_factor = 0.5
        self.items = 0

    def get_index(self,val,table_size):
        return hash(str(val))%table_size

    def grow(self):
        new_table_size = self.table_size * 2
        new_table = [None]*new_table_size

        for i in range(self.table_size):
            if not self.table[i]: continue
            cur_LL = self.table[i]
            cur = cur_LL.head.nxt

            while cur != cur_LL.tail:
                index = self.get_index(cur.val,new_table_size)
                if not new_table[index]: new_table[index] = LL()
                new_table[index].append(cur.val)
                cur = cur.nxt

        self.table = new_table
        self.table_size = new_table_size

    def add(self, val):
        if self.items/self.table_size > self.max_load_factor: self.grow()

        index = self.get_index(val,self.table_size)
        if not self.table[index]: self.table[index] = LL()
        
        cur_LL = self.table[index]
        node = cur_LL.find(val)
        
        if node: node.val = val
        else:
            cur_LL.append(val)
            self.items += 1

    def exists(self, val):
        index = self.get_index(val,self.table_size)
        if not self.table[index]: return False
        
        node = self.table[index].find(val)
        return node is not None

    def remove(self, val):
        index = self.get_index(val,self.table_size)
        if not self.table[index]: return
        
        node = self.table[index].remove(val)
        if node: self.items -= 1
