class RateLimiter:
    def __init__(self, expire):
        self.expire = expire
        self.last_times = defaultdict(lambda: -inf)

    def limit(self, uid, timestamp):
        if timestamp - self.last_times[uid] < self.expire:
            return True
        else:
            self.last_times[uid] = timestamp
            return False
