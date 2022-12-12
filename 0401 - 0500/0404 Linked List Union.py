# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, ll0, ll1):
        ans = LLNode(None)
        cur = ans

        while ll0 and ll1:
            if ll0.val < ll1.val:
                if ll0.val != cur.val:
                    cur.next = LLNode(ll0.val)
                    cur = cur.next
                ll0 = ll0.next
            else:
                if ll1.val != cur.val:
                    cur.next = LLNode(ll1.val)
                    cur = cur.next
                ll1 = ll1.next

        
        while ll0:
            if ll0.val != cur.val:
                cur.next = LLNode(ll0.val)
                cur = cur.next
            ll0 = ll0.next

        while ll1:
            if ll1.val != cur.val:
                cur.next = LLNode(ll1.val)
                cur = cur.next
            ll1 = ll1.next

        return ans.next
