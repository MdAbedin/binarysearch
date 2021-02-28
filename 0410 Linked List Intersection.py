# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l0, l1):
        ans_head = LLNode(0)
        ans_cur = ans_head

        while l0 and l1:
          if l0.val < l1.val:
            l0 = l0.next
          elif l1.val < l0.val:
            l1 = l1.next
          else:
            ans_cur.next = LLNode(l0.val)
            ans_cur = ans_cur.next
            l0 = l0.next
            l1 = l1.next

        return ans_head.next
