# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root: return 0

        cur = root
        level = 0

        while cur:
            cur = cur.right
            level += 1

        ans = 2**level - 1
        l,r = 2**level,2**(level+1)-1

        def exists(i):
            cur = root
            binary = list(bin(i)[3:][::-1])
            
            while binary:
                if binary[-1] == "0": cur = cur.left
                else: cur = cur.right
                if not cur: return False
                binary.pop()

            return True

        while l <= r:
            m = (l+r)//2

            if exists(m):
                ans = m
                l = m+1
            else:
                r = m-1

        return ans
