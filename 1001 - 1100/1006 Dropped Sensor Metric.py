class Solution:
    def solve(self, a, b):
        for i in range(len(a)):
            if a[i] != b[i]:
                if a[i:-1] == b[i+1:]:
                    return b[i]
                else:
                    return a[i]
