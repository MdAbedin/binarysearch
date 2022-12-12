class Solution:
    def solve(self, target):
        if not target: return True
        if len(target) == 1: return target == [1]
        
        cur_sum = sum(target)
        pq = [-x for x in target]
        heapify(pq)

        while pq[0] != -1:
            max_ = -heappop(pq)
            next_max = -pq[0]
            left_sum = cur_sum - max_
            prev_eq = max_ - ceil((max_ - next_max)/left_sum)*left_sum
            prev_less = max_ - ceil((max_ - next_max + 1)/left_sum)*left_sum
            
            if prev_eq != 1 and (prev_less < 1 or prev_less >= max_): return False

            cur_sum = cur_sum - max_ + prev_less
            heappush(pq, -prev_less)

        return True
