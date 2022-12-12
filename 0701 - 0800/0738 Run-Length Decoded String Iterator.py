class RunLengthDecodedIterator:
    def __init__(self, s):
        tokens = re.split('([abcdefghijklmnopqrstuvwxyz])',s)
        self.data = [[int(tokens[i]), tokens[i+1]] for i in range(0,len(tokens)-1,2)]
        self.i = 0

    def next(self):
        ans = self.data[self.i][1]
        self.data[self.i][0] -= 1
        if self.data[self.i][0] == 0: self.i += 1
        
        return ans


    def hasnext(self):
        return self.i < len(self.data)
