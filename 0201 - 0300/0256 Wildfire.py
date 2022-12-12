class Solution:
    def solve(self, matrix):
        if not matrix:
            return 0

        if not matrix[0]:
            return 0

        fire_frontier_bfs = deque()
        num_on_fire = 0
        total_trees = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 2:
                    fire_frontier_bfs.append([r,c])
                    num_on_fire += 1
                    total_trees += 1
                elif matrix[r][c] == 1:
                    total_trees += 1
        
        days_used = 0

        while num_on_fire < total_trees:
            if not fire_frontier_bfs:
                return -1
                
            for i in range(len(fire_frontier_bfs)):
                cr,cc = fire_frontier_bfs.popleft()

                for nr,nc in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:
                    if 0<=nr<len(matrix) and 0<=nc<len(matrix[0]) and matrix[nr][nc] == 1:
                        matrix[nr][nc] = 2
                        fire_frontier_bfs.append([nr,nc])
                        num_on_fire += 1

            days_used += 1

        return days_used
