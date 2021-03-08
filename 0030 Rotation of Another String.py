class Solution:
    def solve(self, s0, s1):
        if Counter(s0) != Counter(s1): return False

        for i in range(len(s0)):
            if all(s1[i+j] == s0[j] for j in range(len(s0)-i)) and all(s1[j] == s0[len(s0)-i+j] for j in range(i)): return True

        return False
