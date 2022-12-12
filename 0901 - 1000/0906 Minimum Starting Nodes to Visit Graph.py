class Solution:
    def solve(self, edges):
        nodes = {node for edge in edges for node in edge}
        has_incoming = {edge[1] for edge in edges}
        return [node for node in sorted(list(nodes)) if node not in has_incoming]
