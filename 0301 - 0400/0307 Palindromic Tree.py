# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        ans = []
        iot = deque([[root,1]])

        while iot:
            cur, t = iot.popleft()

            if t == 1:
                if cur.right: iot.appendleft([cur.right,1])
                iot.appendleft([cur,2])
                if cur.left: iot.appendleft([cur.left,1])
            else:
                ans.append(cur.val)

        return all(ans[i] == ans[-1*i-1] for i in range(len(ans)//2))
