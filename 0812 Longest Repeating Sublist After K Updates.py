class Solution:
    def ans(self,locs,k,N):
        max_ans = 0
        cur_ans = 0
        remaining = k
        last = len(locs)-1

        for i in range(len(locs)-1,-1,-1):
            last = min(last,i)
            last_used = 0
            include_next = False

            while remaining > 0 and last >= 0:
                cur_ans += locs[last][1]
                gap = locs[last][0]-locs[last][1]+1-(locs[last-1][0] if last-1>=0 else -1)-1
                used = min(remaining,gap)
                remaining -= used
                last_used = used
                include_next = used == gap

                if remaining > 0: last -= 1

            last = max(last,0)
            max_ans = max(max_ans,cur_ans+k-remaining+(0 if last == 0 or not include_next else locs[last-1][1]))
            max_ans = max(max_ans, min(N,cur_ans+k))

            remaining += min(k,locs[i][0]-locs[i][1]+1-(locs[i-1][0] if i-1>=0 else -1)-1)
            cur_ans -= locs[i][1]
            if last != i:
                remaining += last_used
                cur_ans -= locs[last][1]

        return max(max_ans,min(N,locs[0][1]+k),min(N,locs[-1][1]+k))

    def helper(self, nums, k):
        if not nums: return 0

        locs = defaultdict(list)

        for i in range(len(nums)):
            if not locs[nums[i]]: locs[nums[i]].append([i,1])
            elif i == locs[nums[i]][-1][0]+1:
                locs[nums[i]][-1][0] = i
                locs[nums[i]][-1][1] += 1
            else:
                locs[nums[i]].append([i,1])
        
        if k == 0: return max(pair[1] for val in locs.values() for pair in val)

        return max(self.ans(locs[key],k,len(nums)) for key in locs)

    def solve(self,nums,k):
        return max(self.helper(nums,k),self.helper(nums[::-1],k))
