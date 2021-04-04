class Solution:
    @cache
    def helper(self,i,j):
        if -1 in [i,j]: return max(i,j)+1
        return min(self.helper(i-1,j-1)+(1 if self.a[i] != self.b[j] else 0),self.helper(i-1,j)+1,self.helper(i,j-1)+1)

    def solve(self, a, b):
        self.a,self.b = a,b
        return self.helper(len(a)-1,len(b)-1)
