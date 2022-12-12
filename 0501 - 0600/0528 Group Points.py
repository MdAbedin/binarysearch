class Solution:
    def solve(self, points, k):
        parents = list(range(len(points)))

        def find(x):
            if x == parents[x]: return x;
            parents[x] = find(parents[x])
            return parents[x]

        def union(a,b):
            a,b = find(a), find(b)
            if a != b: parents[b] = a

        def dist_sq(x1,y1,x2,y2): return (x2-x1)**2 + (y2-y1)**2

        for i in range(len(points)):
            for j in range(i):
                if dist_sq(*points[i], *points[j]) <= k**2:
                    union(i,j)

        return len(set(find(x) for x in range(len(points))))
