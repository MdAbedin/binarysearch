class Solution:
    def solve(self, lst, p):
        for i in range(len(lst)):
            if p[i] != i:
                cur = i
                char = lst[i]

                while p[cur] != cur:
                    new_cur = p[cur]
                    new_char = lst[new_cur]
                    
                    lst[new_cur] = char
                    p[cur] = cur

                    cur,char = new_cur,new_char

        return lst
