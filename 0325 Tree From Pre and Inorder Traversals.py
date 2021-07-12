# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, preorder, inorder):
        plocs = {x:i for i,x in enumerate(preorder)}
        ilocs = {x:i for i,x in enumerate(inorder)}

        def helper(l,r,l2,r2):
            if l > r: return None
            
            root = preorder[l]
            lsize = ilocs[root]-l2

            return Tree(root, helper(l+1,l+lsize,l2,ilocs[root]-1), helper(l+lsize+1,r,l2+lsize+1,r2))
        
        return helper(0,len(preorder)-1,0,len(preorder)-1)
