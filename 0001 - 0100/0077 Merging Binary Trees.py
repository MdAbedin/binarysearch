# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node0, node1):
        if not node0: return node1
        if not node1: return node0

        ans_root = Tree(node0.val + node1.val)
        bfs = deque([[ans_root, node0, node1]])

        while bfs:
          a,b,c = bfs.popleft()

          if b.left or c.left:
            a.left = Tree((b.left.val if b.left else 0) + (c.left.val if c.left else 0))
            a2,b2,c2 = a.left,b.left if b.left else Tree(0),c.left if c.left else Tree(0)
            bfs.append([a2,b2,c2])
          
          if b.right or c.right:
            a.right = Tree((b.right.val if b.right else 0) + (c.right.val if c.right else 0))
            a2,b2,c2 = a.right,b.right if b.right else Tree(0),c.right if c.right else Tree(0)
            bfs.append([a2,b2,c2])

        return ans_root
