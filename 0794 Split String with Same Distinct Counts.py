class Solution:
    def solve(self, s):
        l_counts = defaultdict(int)
        l_count = 0
        r_counts = Counter(s)
        r_count = len(r_counts)
        ans = 0

        for i in range(len(s)):
            l_counts[s[i]] += 1
            if l_counts[s[i]] == 1:
                l_count += 1

            r_counts[s[i]] -= 1
            if r_counts[s[i]] == 0:
                r_count -= 1

            ans += l_count == r_count

        return ans
