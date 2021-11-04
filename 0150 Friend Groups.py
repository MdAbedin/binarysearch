class Solution:
    def solve(self, friends):
        ans = 0

        seen = set()

        for i in range(len(friends)):
            if i in seen: continue

            ans += 1
            dfs = [i]

            while dfs:
                cur = dfs.pop()
                
                for nei in friends[cur]:
                    if nei not in seen:
                        seen.add(nei)
                        dfs.append(nei)

        return ans
