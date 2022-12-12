class Solution:
    def solve(self, s, k):
        if len(s) < k: return 0

        stats = defaultdict(int)
        chars = deque(" " + s[:k-1])
        ans = 0

        for i in range(k-1,len(s)):
            chars.popleft()
            chars.append(s[i])
            string = "".join(chars)
            stats[string] += 1

            if stats[string] == 2: ans += 1

        return ans
