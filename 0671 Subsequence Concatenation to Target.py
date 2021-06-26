class Solution:
    def solve(self, source, target):
        locs = defaultdict(list)

        for i,char in enumerate(source):
            locs[char].append(i)

        ans = 0
        cur = len(source)

        for char in target:
            if char not in locs:
                return -1

            nxt = bisect_left(locs[char],cur+1)
            if nxt == len(locs[char]):
                nxt = 0
                ans += 1

            cur = locs[char][nxt]

        return ans
