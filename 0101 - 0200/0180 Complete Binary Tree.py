# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return True
        bfs = deque([root])
        stopped = False
        
        while bfs:
            for _ in range(len(bfs)):
                cur = bfs.popleft()

                if cur.left:
                    if stopped: return False
                    bfs.append(cur.left)
                else: stopped = True

                if cur.right:
                    if stopped: return False
                    bfs.append(cur.right)
                else: stopped = True

        return True
