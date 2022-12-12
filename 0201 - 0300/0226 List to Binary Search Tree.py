# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, l, r):
      if l > r: return None

      mid = (l+r+1)//2
      root = Tree(self.nums[mid])
      root.left = self.helper(l,mid-1)
      root.right = self.helper(mid+1,r)

      return root

    def solve(self, nums):
      self.nums = nums

      return self.helper(0,len(nums)-1)  
