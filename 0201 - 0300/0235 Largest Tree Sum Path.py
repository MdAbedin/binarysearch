class Solution:
    def helper(self,root):
        if not root: return 0
        l,r = self.helper(root.left), self.helper(root.right)
        self.ans = max(self.ans, l+r+root.val)
        return max(0,root.val + max(l,r))

    def solve(self, root):
        self.ans = 0
        self.helper(root)
        return self.ans
