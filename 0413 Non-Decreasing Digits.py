class Solution:
    def solve(self, n):
        list_n = list(str(n))
        decrease_i = 0

        for i in range(1,len(list_n)):
            if list_n[i] < list_n[i-1]:
                list_n[decrease_i] = chr(ord(list_n[decrease_i])-1)
                for j in range(decrease_i+1,len(list_n)):
                    list_n[j] = "9"
                break
            elif list_n[i] > list_n[i-1]:
                decrease_i = i

        return int("".join(list_n))
