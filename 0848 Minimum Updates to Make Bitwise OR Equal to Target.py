class Solution:
    def solve(self, a, b, target):
        a = list(map(int,bin(a)[2:].rjust(35,'0')))
        b = list(map(int,bin(b)[2:].rjust(35,'0')))
        target = list(map(int,bin(target)[2:].rjust(35,'0')))

        return sum(a[i]==b[i]==0 if target[i]==1 else a[i]+b[i] for i in range(35))
