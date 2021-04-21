class BooleanArray:
    def __init__(self):
        self.locs = set()
        self.is_true = False

    def setTrue(self, i):
        if not self.is_true:
            self.locs.add(i)
        else:
            self.locs.discard(i)
        
    def setFalse(self, i):
        if self.is_true:
            self.locs.add(i)
        else:
            self.locs.discard(i)

    def setAllTrue(self):
        self.locs = set()
        self.is_true = True

    def setAllFalse(self):
        self.locs = set()
        self.is_true = False
        

    def getValue(self, i):
        if self.is_true:
            return i not in self.locs
        else:
            return i in self.locs
