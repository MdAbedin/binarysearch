# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, a, b, lo, hi):
        if not a: return b
        
        a_lo_prev = None if lo == 0 else a

        for i in range(lo-1):
            a_lo_prev = a_lo_prev.next

        a_hi_next = a

        for i in range(hi+1):
            a_hi_next = a_hi_next.next

        b_end = b

        while b_end and b_end.next:
            b_end = b_end.next

        if not a_lo_prev and not a_hi_next: return b
        if not a_lo_prev:
            if b_end:
                b_end.next = a_hi_next
                return b
            else: return a_hi_next
        if not a_hi_next:
            a_lo_prev.next = b
            return a

        a_lo_prev.next = b
        b_end.next = a_hi_next

        return a
