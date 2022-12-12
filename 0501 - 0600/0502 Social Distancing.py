class Solution:
    def solve(self, s, k):
        dists_to_left_x = []
        rightmost_x = -inf

        for i in range(len(s)):
            if s[i] == "x":
                dists_to_left_x.append(inf)
                rightmost_x = i
            else:
                dists_to_left_x.append(i-rightmost_x)

        dists_to_right_x = []
        leftmost_x = inf

        for i in range(len(s)-1,-1,-1):
            if s[i] == "x":
                dists_to_right_x.append(inf)
                leftmost_x = i
            else:
                dists_to_right_x.append(leftmost_x-i)

        dists_to_right_x.reverse()
        
        return any(s[i]=="." and min(dists_to_left_x[i], dists_to_right_x[i]) >= k for i in range(len(s)))
