# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target, radius):
        neis = defaultdict(list)
        dfs = [[root,None]]

        while dfs:
            cur, parent = dfs.pop()
            
            if parent is not None:
                neis[cur.val].append(parent)

            if cur.left:
                dfs.append([cur.left, cur.val])
                neis[cur.val].append(cur.left.val)
            if cur.right:
                dfs.append([cur.right, cur.val])
                neis[cur.val].append(cur.right.val)

        bfs = deque([target])
        seen = {target}

        for level in range(radius):
            for i in range(len(bfs)):
                cur = bfs.popleft()

                for nei in neis[cur]:
                    if nei not in seen:
                        seen.add(nei)
                        bfs.append(nei)

        return sorted(list(bfs))
