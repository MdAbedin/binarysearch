class Solution:
    def solve(self, a, b):
        if a == a[::-1]: return True
        
        for i in range(len(a)):
            if a[i] != b[~i]:
                s = a[:i] + b[i:]
                return s == s[::-1]

        return True
