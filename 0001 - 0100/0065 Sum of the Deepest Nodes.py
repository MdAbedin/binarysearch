# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return 0
        
        ans = 0
        bfs = deque([root])

        while bfs:
            cur_ans = 0

            for i in range(len(bfs)):
                cur = bfs.popleft()
                cur_ans += cur.val

                if cur.left: bfs.append(cur.left)
                if cur.right: bfs.append(cur.right)

            ans = cur_ans

        return ans
