class Solution:
    def solve(self, nums):
        if not nums:
            return 0
            
        g = defaultdict(list)

        for i in range(len(nums)):
            g[nums[i]].append(i)

        bfs = deque([-1])
        seen = {-1}
        ans = 0

        while bfs:
            ans += 1

            for i in range(len(bfs)):
                cur = bfs.popleft()
                
                for child in g[cur]:
                    if child not in seen:
                        seen.add(child)
                        bfs.append(child)

        return ans-1
