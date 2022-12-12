# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        ans = LLNode(0,node)
        l = ans
        cur = node
        prev = ans

        while cur:
            if cur.val < k:
                if l.next == cur:
                    l = l.next
                    prev = cur
                    cur = cur.next
                else:
                    prev.next = cur.next
                    cur.next = l.next
                    l.next = cur
                    l = l.next
                    cur = prev.next
            else:
                prev = cur
                cur = cur.next

        cur = l.next
        prev = l
        
        while cur:
            if cur.val == k:
                if l.next == cur:
                    l = l.next
                    prev = cur
                    cur = cur.next
                else:
                    prev.next = cur.next
                    cur.next = l.next
                    l.next = cur
                    l = l.next
                    cur = prev.next
            else:
                prev = cur
                cur = cur.next

        return ans.next
