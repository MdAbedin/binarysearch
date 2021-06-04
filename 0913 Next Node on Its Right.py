# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, tree, target):
        if not tree:
            return None

        bfs = deque([tree])

        while bfs:
            L = len(bfs)

            for i in range(len(bfs)):
                cur = bfs.popleft()

                if cur.val == target:
                    return bfs[0] if i+1 < L else None

                if cur.left:
                    bfs.append(cur.left)

                if cur.right:
                    bfs.append(cur.right)

        return None
