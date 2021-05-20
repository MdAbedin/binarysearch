class Solution:
    def solve(self, genes):
        ans = 0
        seen = set()
        genes = set(genes)

        for gene in genes:
            if gene in seen:
                continue

            ans += 1
            dfs = [gene]
            seen.add(gene)

            while dfs:
                cur = dfs.pop()
                cur_list = list(cur)

                for i in range(len(cur)):
                    for char in ["A","C","G","T"]:
                        if char == cur[i]: continue

                        cur_list[i] = char
                        new_gene = "".join(cur_list)
                        
                        if new_gene in genes and new_gene not in seen:
                            seen.add(new_gene)
                            dfs.append(new_gene)

                    cur_list[i] = cur[i]
            
        return ans
