class Solution:
    def solve(self, words):
        groups = defaultdict(list)

        for word in words:
            for key in groups:
                if len(word)==len(key) and any(all(word[j]==key[j-i] for j in range(i,len(word))) and all(word[j]==key[len(word)-i+j] for j in range(i)) for i in range(len(word))):
                    groups[key].append(word)
                    break
            else:
                groups[word].append(word)

        return len(groups)
