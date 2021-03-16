class Solution:
    def solve(self, s):
        narysearch = "narysearch"
        locs = defaultdict(set)
        for i in range(len(s)):
            locs[s[i]].add(i)
        
        for b_loc in locs['b']:
            for i_loc in locs['i']:
                if i_loc < b_loc: continue
                
                d = i_loc - b_loc

                if all(i_loc+d*(j+1) in locs[narysearch[j]] for j in range(len(narysearch))): return True

        return False
