class Solution:
    def solve(self, orders):
        info = defaultdict(lambda: "none")

        for order in orders:
            char = order[0]
            num = int(order[1:])
            
            if char == "P":
                if info[num] != "none":
                    return False
                info[num] = "P"
            else:
                if info[num] != "P":
                    return False
                info[num] = "D"

        return all(v == "D" for v in info.values())
