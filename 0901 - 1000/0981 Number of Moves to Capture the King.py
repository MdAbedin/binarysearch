class Solution:
    def solve(self, board):
        bfs = deque()
        seen = set()
        for y,row in enumerate(board):
            if 2 in row:
                bfs.append([y,row.index(2),0])
                seen.add((y,row.index(2)))
        
        while bfs:
            cy,cx,m = bfs.popleft()

            for ny,nx in [[cy-2,cx-1],[cy-2,cx+1],[cy-1,cx+2],[cy+1,cx+2],[cy+2,cx+1],[cy+2,cx-1],[cy+1,cx-2],[cy-1,cx-2]]:
                if 0<=ny<len(board) and 0<=nx<len(board[0]) and (ny,nx) not in seen:
                    if board[ny][nx] == 1: return m+1
                    bfs.append([ny,nx,m+1])
                    seen.add((ny,nx))

        return -1
