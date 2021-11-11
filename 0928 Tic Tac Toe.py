class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.diag1 = 0
        self.diag2 = 0

    def move(self, r, c, me):
        add = 1 if me else -1
        self.rows[r] += add
        self.cols[c] += add
        if r == c: self.diag1 += add
        if r == self.n-1-c: self.diag2 += add

        if abs(self.rows[r]) == self.n: return self.rows[r]//self.n
        if abs(self.cols[c]) == self.n: return self.cols[c]//self.n
        if abs(self.diag1) == self.n: return self.diag1//self.n
        if abs(self.diag2) == self.n: return self.diag2//self.n

        return 0
