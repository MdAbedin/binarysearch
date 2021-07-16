class Trie:
    def __init__(self,char="",end=False):
        self.char = char
        self.end = end
        self.nexts = dict()

    def add(self, s):
        cur = self

        for i in range(len(s)):
            if s[i] not in cur.nexts: cur.nexts[s[i]] = Trie(s[i])
            cur = cur.nexts[s[i]]

        cur.end = True

    def exists(self, word):
        cur = self
        for char in word:
            if char not in cur.nexts: return False
            cur = cur.nexts[char]
        return cur.end

    def startswith(self, p):
        cur = self
        for char in p:
            if char not in cur.nexts: return False
            cur = cur.nexts[char]
        return True
