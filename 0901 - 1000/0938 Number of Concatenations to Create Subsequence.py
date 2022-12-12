class Solution:
    def solve(self, s, t):
        s_chars = set(s)
        if not all(char in s_chars for char in t): return -1

        ans = 1
        used = 0
        last = 0

        while used < len(t):
            # print(used)
            i = s.find(t[used],last)
            # print(i)
            if i == -1:
                last = 0
                ans += 1
                continue
            else:
                last = i+1
                used += 1
            # print(ans)
            # print()

        return ans
