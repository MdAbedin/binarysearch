class Solution:
    def solve(self, s0, s1):
        words0 = {word.upper() for word in s0.split()}
        words1 = {word.upper() for word in s1.split()}

        return sum(word in words1 for word in words0)
