class Solution:
    def solve(self, start, end):
        if end <= start: return start - end
        if end%2 == 1: return 2 + self.solve(start, (end+1)//2)
        return 1 + self.solve(start, end//2)
