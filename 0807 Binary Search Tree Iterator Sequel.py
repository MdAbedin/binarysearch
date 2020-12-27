# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root):
        dfs = [root]
        nums = []
        while dfs:
          cur = dfs.pop()
          nums.append(cur.val)
          if cur.left: dfs.append(cur.left)
          if cur.right: dfs.append(cur.right)
        nums.sort()
        self.nums = nums
        self.i = -1

    def next(self):
        self.i += 1
        return self.nums[self.i]

    def hasnext(self):
        return self.i < len(self.nums)-1

    def prev(self):
        self.i -= 1
        return self.nums[self.i]

    def hasprev(self):
        return self.i > 0
