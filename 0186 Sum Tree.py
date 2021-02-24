# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return True

        bfs = deque([root])

        while bfs:
          cur = bfs.popleft()
          S = 0
          
          if cur.left:
            bfs.append(cur.left)
            S += cur.left.val

          if cur.right:
            bfs.append(cur.right)
            S += cur.right.val

          if (cur.left or cur.right) and S != cur.val: return False

        return True
