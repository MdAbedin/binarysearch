class Solution:
    def solve(self, s0, s1):
        if len(s0) == len(s1):
            return sum(c0 != c1 for c0,c1 in zip(s0,s1)) <= 1

        if abs(len(s0) - len(s1)) != 1:
            return False

        if len(s1) > len(s0):
            s0,s1 = s1,s0

        if s0[:-1] == s1:
            return True

        for i in range(len(s0)):
            if s0[i] != s1[i]:
                return s0[:i] == s1[:i] and s0[i+1:] == s1[i:]
