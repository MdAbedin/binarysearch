# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        bfs = deque([root])

        while bfs:
          is_leaf = not bfs[0].left and not bfs[0].right

          for i in range(len(bfs)):
            cur = bfs.popleft()

            if (not cur.left and not cur.right) != is_leaf: return False

            if cur.left: bfs.append(cur.left)
            if cur.right: bfs.append(cur.right)

        return True
