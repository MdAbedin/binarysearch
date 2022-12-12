# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root):
        order = []
        dfs = [root]

        while dfs:
            cur = dfs.pop()
            order.append(cur.val)

            if cur.left:
                dfs.append(cur.left)

            if cur.right:
                dfs.append(cur.right)

        order.sort()
        self.order = order
        self.i = 0

    def next(self):
        ans = self.order[self.i]
        self.i += 1
        
        return ans

    def hasnext(self):
        return self.i < len(self.order)
