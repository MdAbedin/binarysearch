class Solution:
    def solve(self, requests):
        counts = defaultdict(lambda: [0,0])
        
        for t,d in requests:
            counts[t][d] += 1
        
        data = sorted(counts.items())
        ans = []
        cur_t = 0
        cur_d = 1

        for t,ds in data:
            if t > cur_t: cur_d = 1
            cur_t = max(cur_t, t)
            other_d = 1-cur_d

            for person in range(ds[cur_d]):
                ans.append([cur_t,cur_d])
                cur_t += 1

            for person in range(ds[other_d]):
                ans.append([cur_t,other_d])
                cur_d = other_d
                cur_t += 1

        return ans
