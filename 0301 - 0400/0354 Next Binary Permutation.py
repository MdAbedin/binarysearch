class Solution:
    def solve(self, n):
        binary = ["0"]+list(bin(n)[2:])
        zero_i, one_i = -1, -1

        for i in range(len(binary)-1,-1,-1):
            if binary[i] == "1": one_i = i
            if one_i != -1 and binary[i] == "0":
                zero_i = i
                break
        
        binary[zero_i] = "1"
        binary[one_i] = "0"

        right_1s = binary[one_i+1:].count("1")
        binary = binary[:one_i+1] + ["0"]*(len(binary) - one_i - 1 - right_1s) + ["1"]*right_1s

        return int("".join(binary), 2)
