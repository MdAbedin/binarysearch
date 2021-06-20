class Solution:
    def solve(self, s):
        return sum(3 if count%3 == 1 else count%3 for count in Counter(s).values()) == 2
