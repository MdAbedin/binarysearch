class Solution:
    def solve(self, matrix):
        leaders = {(r,c):(r,c) for r in range(len(matrix)) for c in range(len(matrix[0])) if matrix[r][c] == 1}
        followers = {(r,c):[(r,c)] for r in range(len(matrix)) for c in range(len(matrix[0])) if matrix[r][c] == 1}

        for r in range(len(matrix)):
            latest = None
            
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    continue

                if latest is None:
                    latest = (r,c)
                    continue

                new_leader = leaders[latest]
                old_leader = leaders[r,c]
                latest = (r,c)
                
                if new_leader == old_leader:
                    continue

                if len(followers[new_leader]) < len(followers[old_leader]):
                    new_leader, old_leader = old_leader, new_leader

                for follower in followers[old_leader]:
                    leaders[follower] = new_leader
                    followers[new_leader].append(follower)

                followers[old_leader] = []
                

        for c in range(len(matrix[0])):
            latest = None
            
            for r in range(len(matrix)):
                if matrix[r][c] == 0:
                    continue

                if latest is None:
                    latest = (r,c)
                    continue

                new_leader = leaders[latest]
                old_leader = leaders[r,c]
                latest = (r,c)

                if new_leader == old_leader:
                    continue

                if len(followers[new_leader]) < len(followers[old_leader]):
                    new_leader, old_leader = old_leader, new_leader

                for follower in followers[old_leader]:
                    leaders[follower] = new_leader
                    followers[new_leader].append(follower)

                followers[old_leader] = []

        return len(set(leaders.values()))
