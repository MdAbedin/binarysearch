class Solution:
    def solve(self, s0, s1):
        if len(s0) != len(s1)+1: return False

        for i in range(len(s1)):
            if s1[i] != s0[i]:
                if s0[i+1:] == s1[i:]:
                    return True
                break

        return s0.startswith(s1)
