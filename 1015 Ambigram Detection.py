class Solution:
    def solve(self, s, pairs):
        letters = set(ascii_lowercase)
        leaders = {letter:letter for letter in letters}
        followers = {letter:[letter] for letter in letters}

        for a,b in pairs:
            if leaders[a] == leaders[b]: continue
            
            if len(followers[a]) < len(followers[b]): a,b = b,a
            old_leader = leaders[b]
            new_leader = leaders[a]

            for follower in followers[old_leader]:
                leaders[follower] = new_leader
                followers[new_leader].append(follower)

            followers[old_leader] = []

        return all(leaders[s[i]]==leaders[s[~i]] for i in range(len(s)))
