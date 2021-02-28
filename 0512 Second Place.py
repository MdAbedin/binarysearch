# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        last_leaf_level = None
        bfs = deque([root])
        depth = 0

        while bfs:
          is_last_level = True
          new_last_leaf_level = None

          for i in range(len(bfs)):
            cur = bfs.popleft()

            if not cur.left and not cur.right:
              new_last_leaf_level = depth

            if cur.left:
              is_last_level = False
              bfs.append(cur.left)

            if cur.right:
              is_last_level = False
              bfs.append(cur.right)

          if is_last_level: return last_leaf_level
          if new_last_leaf_level: last_leaf_level = new_last_leaf_level
          depth += 1
