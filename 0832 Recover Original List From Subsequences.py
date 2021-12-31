class Solution:
    def solve(self, lists):
        ans = []
        counts = defaultdict(int)
        locs = defaultdict(list)

        for r in range(len(lists)):
            for c in range(len(lists[r])):
                counts[lists[r][c]] += 0 if c == 0 else 1
                locs[lists[r][c]].append([r,c])

        start = next(num for num in counts if counts[num] == 0)

        while True:
            ans.append(start)
            counts.pop(start)

            for r,c in locs[start]:
                if c+1 < len(lists[r]):
                    counts[lists[r][c+1]] -= 1
                    if counts[lists[r][c+1]] == 0: start = lists[r][c+1]

            if not counts: break

        return ans
