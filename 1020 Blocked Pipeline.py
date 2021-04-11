class Solution:
    def solve(self, n, requests):
        blocks = set()
        problems = set()
        ans = 0

        for r,c,t in requests:
            if t == 1:
                blocks.add((r,c))

                for r2,c2 in [(1-r,c+1),(1-r,c-1),(1-r,c)]:
                    if (r2,c2) in blocks:
                        problems.add(tuple(sorted(map(tuple,[[r,c],[r2,c2]]))))

                if not problems: ans += 1
            else:
                blocks.discard((r,c))

                for r2,c2 in [(1-r,c+1),(1-r,c-1),(1-r,c)]:
                    if (r2,c2) in blocks:
                        problems.discard(tuple(sorted(map(tuple,[[r,c],[r2,c2]]))))

                if not problems: ans += 1

        return ans
