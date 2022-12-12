# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        ans = []
        level = 0
        bfs = deque([root])

        while bfs:
          level_vals = [x.val for x in bfs]
          ans += level_vals if level%2 == 0 else level_vals[::-1]
          
          for i in range(len(bfs)):
            cur = bfs.popleft()

            if cur.left: bfs.append(cur.left)
            if cur.right: bfs.append(cur.right)

          level +=1

        return ans
