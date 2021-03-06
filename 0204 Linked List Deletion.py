# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, target):
        ans_head = LLNode(0)
        ans_cur = ans_head
        cur = node

        while cur:
          if cur.val != target:
            ans_cur.next = LLNode(cur.val)
            ans_cur = ans_cur.next

          cur = cur.next

        return ans_head.next
