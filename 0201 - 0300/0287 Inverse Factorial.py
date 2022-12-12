class Solution:
    def solve(self, a):
        a2 = 1
        n = 1

        while a2 < a:
            n += 1
            a2 *= n
            
        return n if a2 == a else -1
