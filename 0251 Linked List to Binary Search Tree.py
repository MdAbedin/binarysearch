# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        if not node: return None
        if not node.next: return Tree(node.val)

        len_cur = node
        length = 0

        while len_cur:
            length += 1
            len_cur = len_cur.next

        prev = node
        cur = node.next

        for i in range(floor(length/2)-1):
            prev = prev.next
            cur = cur.next

        prev.next = None

        return Tree(cur.val,self.solve(node),self.solve(cur.next))
