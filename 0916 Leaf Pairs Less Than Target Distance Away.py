# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):
        if not root: return 0
        
        locs = []
        dfs = [[root,1]]
        ans = 0

        while dfs:
            cur,loc = dfs.pop()

            if not cur.left and not cur.right:
                for loc2 in locs:
                    dist = 0
                    loc1 = loc

                    while loc1 != loc2:
                        if loc1 > loc2:
                            loc1 //= 2
                        else:
                            loc2 //= 2

                        dist += 1

                    if dist <= target: ans += 1

                locs.append(loc)

            if cur.left:
                dfs.append([cur.left, loc*2])
            if cur.right:
                dfs.append([cur.right, loc*2+1])

        return ans
