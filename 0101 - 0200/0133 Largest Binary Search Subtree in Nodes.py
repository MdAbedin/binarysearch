# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        is_bst = defaultdict(lambda: True)
        st_sizes = defaultdict(int)
        mins = defaultdict(lambda: inf)
        maxes = defaultdict(lambda: -inf)
        dfs = [[root,1]]
        ans = None

        while dfs:
          cur, t = dfs[-1]

          if t == 1:
            dfs[-1][1] = 2
            if cur.left: dfs.append([cur.left,1])
            if cur.right: dfs.append([cur.right,1])
          else:
            is_bst[cur] = is_bst[cur.left] and is_bst[cur.right] and cur.val > maxes[cur.left] and cur.val < mins[cur.right]
            st_sizes[cur] = 1 + st_sizes[cur.left] + st_sizes[cur.right]
            mins[cur] = min(mins[cur.left] if cur.left else cur.val, cur.val, mins[cur.right] if cur.right else cur.val)
            maxes[cur] = min(maxes[cur.left] if cur.left else cur.val, cur.val, maxes[cur.right] if cur.right else cur.val)
            if is_bst[cur]:
              ans = max(ans, cur, key=lambda x: st_sizes[x])
            dfs.pop()

        return ans
