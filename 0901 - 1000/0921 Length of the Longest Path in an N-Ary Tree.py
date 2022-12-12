class Solution:
    def solve(self, edges):
        children = defaultdict(list)
        roots = {x for pair in edges for x in pair}

        for a,b in edges:
            children[a].append(b)
            roots.discard(b)

        def helper(root):
            if not children[root]: return 1,1

            child_ans = sorted([helper(child) for child in children[root]])

            if len(child_ans) == 1: return child_ans[0][0]+1, max(child_ans[0][1], child_ans[0][0]+1)

            return child_ans[-1][0]+1, max(max(ans[1] for ans in child_ans), child_ans[-1][0] + child_ans[-2][0] + 1)

        return helper(list(roots)[0])[1]
