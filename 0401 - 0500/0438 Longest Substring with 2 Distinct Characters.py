class Solution:
    def solve(self, s):
        counts = defaultdict(int)
        ans = 0
        distincts = 0
        start = 0

        for i in range(len(s)):
            if counts[s[i]] == 0: distincts += 1
            counts[s[i]] += 1

            while distincts > 2:
                if counts[s[start]] == 1: distincts -= 1
                counts[s[start]] -= 1
                start += 1

            ans = max(ans, i-start+1)

        return ans
