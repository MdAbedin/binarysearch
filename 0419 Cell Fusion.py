class Solution:
    def solve(self, cells):
        pq = [-1*x for x in cells]
        heapify(pq)

        while len(pq) > 1:
            a,b = -heappop(pq), -heappop(pq)
            if a != b: heappush(pq, -floor((a+b)/3))

        return -1 if not pq else -pq[0]
