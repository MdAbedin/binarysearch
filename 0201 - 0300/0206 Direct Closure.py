class Solution:
    def solve(self, graph):
        leaders = {i:i for i in range(len(graph))}
        followers = {i:[i] for i in range(len(graph))}

        for a in range(len(graph)):
            for b in graph[a]:
                big_leader = leaders[a]
                small_leader = leaders[b]
                if len(followers[small_leader]) > len(followers[big_leader]): big_leader,small_leader = small_leader, big_leader

                if big_leader == small_leader: continue

                for follower in followers[small_leader]:
                    leaders[follower] = big_leader
                    followers[big_leader].append(follower)

                followers[small_leader] = []

        return [[1 if leaders[i] == leaders[j] else 0 for j in range(len(graph))] for i in range(len(graph))]
