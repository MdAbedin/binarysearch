class Solution:
    def solve(self, a, b):
        if min(len(a),len(b))*6 < max(len(a),len(b))*1: return -1
        
        if sum(b) < sum(a): a,b = b,a
        a_sum,b_sum = sum(a),sum(b)
        heapify(a)
        b = [-1*x for x in b]
        heapify(b)
        ans = 0

        while a_sum < b_sum:
            if 6-a[0] > -b[0]-1:
                a_sum += 6-a[0]
                heappop(a)
                heappush(a,6)
            else:
                b_sum -= (-b[0]-1)
                heappop(b)
                heappush(b,-1)

            ans += 1

        return ans
