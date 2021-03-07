class Solution:
    def solve(self, board, word):
        for r in range(len(board)):
            for c in range(len(board[0])-len(word)+1):
                if all(board[r][c+i] == word[i] for i in range(len(word))): return True

        for r in range(len(board)-len(word)+1):
            for c in range(len(board[0])):
                if all(board[r+i][c] == word[i] for i in range(len(word))): return True
                
        return False
