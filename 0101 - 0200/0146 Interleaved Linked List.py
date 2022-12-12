# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l0, l1):
        p1,p2 = l0,l1
        head = LLNode(0)
        ans = head

        while p1 and p2:
          ans.next = p1
          ans = ans.next
          p1 = p1.next
          ans.next = p2
          ans = ans.next
          p2 = p2.next

        while p1:
          ans.next = p1
          ans = ans.next
          p1 = p1.next
          
        while p2:
          ans.next = p2
          ans = ans.next
          p2 = p2.next

        return head.next
