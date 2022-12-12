class Solution:
    def solve(self, nums):
        if len(nums) <= 1: return 0

        locs = defaultdict(list)
        for i,x in enumerate(nums): locs[x].append(i)
        bfs = deque([0])
        steps = 0
        seen = {0}
        seen_vals = {nums[0]}

        while bfs:
            for _ in range(len(bfs)):
                cur = bfs.popleft()

                for nei in locs[nums[cur]]:
                    if nei == len(nums)-1: return steps+1
                    
                    if nei not in seen and ((nei-1 >= 0 and nums[nei-1] not in seen_vals) or (nei+1 < len(nums) and nums[nei+1] not in seen_vals)):
                        seen.add(nei)
                        seen_vals.add(nums[nei])
                        bfs.append(nei)

                for nei in [cur-1,cur+1]:
                    if nei == len(nums)-1: return steps+1
                    
                    if 0<=nei<len(nums) and nei not in seen:
                        seen.add(nei)
                        seen_vals.add(nums[nei])
                        bfs.append(nei)

            steps += 1
