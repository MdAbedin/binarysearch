class WebBrowser:
    def __init__(self, homepage):
        self.history = [homepage]
        self.i = 0

    def visit(self, page):
        while self.i != len(self.history)-1:
            self.history.pop()
        self.history.append(page)
        self.i += 1

    def back(self, n):
        self.i = max(self.i-n, 0)
        return self.history[self.i]

    def forward(self, n):
        self.i = min(self.i+n, len(self.history)-1)
        return self.history[self.i]
