# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root:
            return True

        A, B = 0,0
        A2, B2 = 0,0
        A_color = root.val
        A_level = True
        bfs = deque([root])

        while bfs:
            for i in range(len(bfs)):
                cur = bfs.popleft()

                if cur.val == A_color:
                    A2 += 1
                else:
                    B2 += 1

                if A_level:
                    A += 1
                else:
                    B += 1

                if cur.left:
                    bfs.append(cur.left)
                if cur.right:
                    bfs.append(cur.right)

            A_level = not A_level

        return [A2,B2] in [[A,B], [B,A]]
