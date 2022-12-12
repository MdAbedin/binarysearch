class Solution:
    def solve(self, N, edges):
        N=N+1
        n = defaultdict(list)
        for a,b,t in edges:
          n[a].append([b,t])
          n[b].append([a,t])
        
        d = [float("inf")]*N
        d[0] = 0
        seen = [False]*N
        
        for i in range(N):
          v = -1
          for j in range(N):
            if not seen[j] and (v == -1 or d[j]<d[v]): v=j
          seen[v]=j
          
          for f,t in n[v]:
            if d[v] + t < d[f]: d[f] = d[v]+t
            
        return max(d)
