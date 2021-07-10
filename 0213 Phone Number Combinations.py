class Solution:
    def solve(self, digits):
        mappings = """| 2 | abc  |
| 3 | def  |
| 4 | ghi  |
| 5 | jkl  |
| 6 | mno  |
| 7 | pqrs |
| 8 | tuv  |
| 9 | wxyz |""".replace("|","").split()
        mappings = {mappings[i]:mappings[i+1] for i in range(0,len(mappings),2)}
        return ["".join(e) for e in product(*[list(mappings[x]) for x in digits])]
