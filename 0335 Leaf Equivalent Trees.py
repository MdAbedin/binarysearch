# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root0, root1):
        leaves1 = []
        dfs = [root0]

        while dfs:
          cur = dfs.pop()

          if not cur.left and not cur.right: leaves1.append(cur.val)
          if cur.left: dfs.append(cur.left)
          if cur.right: dfs.append(cur.right)

        leaves2 = []
        dfs = [root1]

        while dfs:
          cur = dfs.pop()

          if not cur.left and not cur.right: leaves2.append(cur.val)
          if cur.left: dfs.append(cur.left)
          if cur.right: dfs.append(cur.right)

        return leaves1 == leaves2
