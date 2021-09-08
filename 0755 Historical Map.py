class HistoricalMap:
    def __init__(self):
        self.data = defaultdict(SortedDict)

    def get(self, key, timestamp):
        return -1 if (i := self.data[key].bisect_right(timestamp)-1) < 0 else self.data[key].peekitem(i)[1]

    def set(self, key, val, timestamp):
        self.data[key][timestamp] = val
