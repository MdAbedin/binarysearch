class Solution:
    def solve(self, nums, k):
        seen = {k}
        dfs = [k]

        while dfs:
            cur = dfs.pop()
            if cur == len(nums)-1: return True
            r = cur+nums[cur]
            l = cur-nums[cur]

            if r < len(nums) and r not in seen:
                seen.add(r)
                dfs.append(r)

            if l >= 0 and l not in seen:
                seen.add(l)
                dfs.append(l)

        return False
