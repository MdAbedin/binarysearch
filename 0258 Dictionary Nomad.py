class Solution:
    def solve(self, dictionary, start, end):
        if len(start) != len(end): return -1
        chars = [{word[i] for word in dictionary} for i in range(len(start))]
        dictionary = set(dictionary)
        seen = set()
        bfs = deque([start])
        level = 1

        while bfs:
          for j in range(len(bfs)):
            cur = bfs.popleft()

            if cur == end: return level

            for i in range(len(cur)):
              for char in chars[i]:
                new = cur[:i] + char + cur[i+1:]
                
                if new not in seen and new in dictionary:
                  seen.add(new)
                  bfs.append(new)

          level += 1

        return -1
