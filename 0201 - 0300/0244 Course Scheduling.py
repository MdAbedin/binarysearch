class Solution:
    def solve(self, courses):
        roots = list(filter(lambda i: courses[i] == [], range(len(courses))))
        if not roots: return not courses

        g = defaultdict(list)
        for i in range(len(courses)):
            for prereq in courses[i]:
                g[prereq].append(i)

        seen = set()

        for root in roots:
            dfs = [root]
            ancestors = set()

            while dfs:
                cur = dfs[-1]

                if cur not in ancestors:
                    ancestors.add(cur)

                    for nei in g[cur]:
                        if nei in ancestors: return False
                        if nei not in seen:
                            seen.add(nei)
                            dfs.append(nei)
                else:
                    dfs.pop()
                    ancestors.remove(cur)

        return True
