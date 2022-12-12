# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root:
            return 0

        bfs = deque([[root,0]])
        ans = 0

        while bfs:
            ans = max(ans, bfs[-1][1]-bfs[0][1]+1)

            for _ in range(len(bfs)):
                cur,i = bfs.popleft()
                
                if cur.left:
                    bfs.append([cur.left,i*2])
                
                if cur.right:
                    bfs.append([cur.right,i*2+1])
                
        return ans
