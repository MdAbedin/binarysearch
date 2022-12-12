# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l0, l1):
        l0_arr, l1_arr = [],[]

        while l0:
            l0_arr.append(l0.val)
            l0 = l0.next

        while l1:
            l1_arr.append(l1.val)
            l1 = l1.next

        ans_val = sum((l0_arr[i]*(10**i) if i < len(l0_arr) else 0)+(l1_arr[i]*(10**i) if i < len(l1_arr) else 0) for i in range(max(len(l0_arr),len(l1_arr))))
        ans_str = str(ans_val)

        ans_head = LLNode(0)
        ans_cur = ans_head

        for i in range(len(ans_str)-1,-1,-1):
            ans_cur.next = LLNode(int(ans_str[i]))
            ans_cur = ans_cur.next

        return ans_head.next
