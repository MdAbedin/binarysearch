class UndergroundTunnel:
    def __init__(self):
        self.ans = defaultdict(lambda: defaultdict(lambda: [0,0]))
        self.data = dict()

    def checkIn(self, userId, station, timestamp):
        self.data[userId] = [station, timestamp]

    def checkOut(self, userId, station, timestamp):
        start_station, start_time = self.data.pop(userId)
        self.ans[start_station][station][0] += timestamp-start_time
        self.ans[start_station][station][1] += 1

    def averageTime(self, start, end):
        return self.ans[start][end][0]/self.ans[start][end][1]
