class Solution:
    def solve(self, a, b):
        min_R = min(len(a),len(b))
        min_C = min(len(a[0]),len(b[0]))
        new = [[0]*(min_C) for i in range(min_R)]

        for r in range(min_R):
            for c in range(min_C):
                if a[r][c] == 1 and b[r][c] == 1: new[r][c] = 1
                elif (a[r][c] == 1) ^ (b[r][c] == 1): new[r][c] = 2

        seen = set()

        for r in range(len(new)):
            for c in range(len(new[0])):
                if new[r][c] == 2 and (r,c) not in seen:
                    new[r][c] = 0
                    dfs = [[r,c]]
                    seen.add((r,c))

                    while dfs:
                        cr,cc = dfs.pop()

                        for nr,nc in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:
                            if 0<=nr<len(new) and 0<=nc<len(new[0]) and new[nr][nc] in [1,2] and (nr,nc) not in seen:
                                new[nr][nc] = 0
                                dfs.append([nr,nc])
                                seen.add((nr,nc))

        seen = set()
        ans = 0


        for r in range(len(new)):
            for c in range(len(new[0])):
                if new[r][c] == 1 and (r,c) not in seen:
                    ans += 1
                    dfs = [[r,c]]

                    while dfs:
                        cr,cc = dfs.pop()

                        for nr,nc in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:
                            if 0<=nr<len(new) and 0<=nc<len(new[0]) and new[nr][nc]==1 and (nr,nc) not in seen:
                                dfs.append([nr,nc])
                                seen.add((nr,nc))

        return ans
