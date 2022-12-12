class Solution:
    def solve(self, board):
        tl = [[0]*len(board[0]) for i in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                tl[r][c] = max(tl[r-1][c] if r-1>=0 else -inf, tl[r][c-1] if c-1>=0 else -inf,board[r][c])

        tr = [[0]*len(board[0]) for i in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])-1,-1,-1):
                tr[r][c] = max(tr[r-1][c] if r-1>=0 else -inf, tr[r][c+1] if c+1<len(board[0]) else -inf,board[r][c])

        bl = [[0]*len(board[0]) for i in range(len(board))]
        for r in range(len(board)-1,-1,-1):
            for c in range(len(board[0])):
                bl[r][c] = max(bl[r+1][c] if r+1<len(board) else -inf, bl[r][c-1] if c-1>=0 else -inf,board[r][c])

        br = [[0]*len(board[0]) for i in range(len(board))]
        for r in range(len(board)-1,-1,-1):
            for c in range(len(board[0])-1,-1,-1):
                br[r][c] = max(br[r+1][c] if r+1<len(board) else -inf, br[r][c+1] if c+1<len(board[0]) else -inf,board[r][c])

        return max(board[r][c] + max(tl[r-1][c-1] if r-1>=0 and c-1>=0 else -inf,tr[r-1][c+1] if r-1>=0 and c+1<len(board[0]) else -inf,bl[r+1][c-1] if r+1<len(board) and c-1>=0 else -inf,br[r+1][c+1] if r+1<len(board) and c+1<len(board[0]) else -inf) for r in range(len(board)) for c in range(len(board[0])))
