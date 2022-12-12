class Solution:
    def solve(self, s1, s2):
        last = 0

        for char in s1:
            if s2.find(char,last) == -1: return False
            last = s2.find(char,last)+1

        return True
