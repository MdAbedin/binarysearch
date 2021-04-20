class Solution:
    def solve(self, a, b, k):
        a.sort()
        b.sort()
        ans = -1
        pq = []
        heappush(pq, [-a[0]*b[0],(0,0),1,1])
        heappush(pq, [-a[-1]*b[-1], (len(a)-1,len(b)-1), -1,-1])
        heappush(pq, [-a[0]*b[-1], (0,len(b)-1), 1,-1])
        heappush(pq, [-a[-1]*b[0], (len(a)-1,0), -1,1])
        used = set()
        found = -1

        while found != k:
            # print(pq)
            y,(i,j),d,d2 = heappop(pq)
            if (i,j) in used: continue
            ans = -y
            used.add((i,j))

            if (i+d,j) not in used and 0<=i+d<len(a): heappush(pq, [-a[i+d]*b[j],(i+d,j),d,d2])
            if (i,j+d2) not in used and 0<=j+d2<len(b): heappush(pq, [-a[i]*b[j+d2],(i,j+d2),d,d2])

            found += 1

        return ans
