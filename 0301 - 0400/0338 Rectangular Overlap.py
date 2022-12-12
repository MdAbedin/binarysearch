class Solution:
    def solve(self,rect0,rect1):
        return ((rect0[1]<=rect1[3]<=rect0[3] or rect0[1]<=rect1[1]<=rect0[3]) and not(rect1[2] <= rect0[0] or rect1[0] >= rect0[2])) or ((rect0[0]<=rect1[0]<=rect0[2] or rect0[0]<=rect1[2]<=rect0[2]) and not(rect1[3] <= rect0[1] or rect1[1] >= rect0[3]))
