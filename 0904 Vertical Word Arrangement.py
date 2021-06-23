class Solution:
    def solve(self, s):
        words = s.split()
        max_len = max(map(len, words))
        words = list(map(lambda x: x.ljust(max_len, " "), words))
        return list(map(lambda x: "".join(x).rstrip(), zip(*words)))
