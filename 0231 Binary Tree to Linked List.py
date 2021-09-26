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
    def solve(self, root):
        ans = LLNode(0)
        cur = ans

        def iot(node):
            nonlocal cur
            if not node: return
            iot(node.left)
            cur.next = LLNode(node.val)
            cur = cur.next
            iot(node.right)

        iot(root)

        return ans.next
