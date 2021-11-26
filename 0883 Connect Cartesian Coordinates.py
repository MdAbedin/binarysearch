class Solution:
    def solve(self, points):
        edges = [[abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j] for i in range(len(points)) for j in range(i+1,len(points))]
        edges.sort()
        parents = list(range(len(points)))
        ans = 0

        def union(x,y,parents):
            x,y = find(x,parents),find(y,parents)
            parents[x] = y

        def find(x,parents):
            if x == parents[x]: return x
            parents[x] = find(parents[x],parents)
            return parents[x]

        for cost,i,j in edges:
            if find(i,parents) != find(j,parents):
                union(i,j,parents)
                ans += cost

        return ans
