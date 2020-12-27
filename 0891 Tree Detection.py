class Solution:
    def solve(self, left, right):
        if any(left[i]==i or right[i]==i for i in range(len(left))) or sum(c != -1 for c in left) + sum(c != -1 for c in right) != len(left)-1: return False
        
        parents = list(set(range(len(left)))-(set(left)|set(right)))
        
        if len(parents) != 1: return False
        
        seen = {parents[0]}
        dfs = [parents[0]]
        while dfs:
          cur = dfs.pop()
          
          if left[cur] != -1:
            if left[cur] not in seen:
              dfs.append(left[cur])
              seen.add(left[cur])
            else:
              return False
          if right[cur] != -1:
            if right[cur] not in seen:
              dfs.append(right[cur])
              seen.add(right[cur])
            else:
              return False
              
        return len(seen) == len(left)
