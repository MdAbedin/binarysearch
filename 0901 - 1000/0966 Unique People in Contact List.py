class Solution:
    def solve(self, contacts):
        used = set()
        ans = 0

        for i in range(len(contacts)):
            new_used = set()
            add = True

            for contact in contacts[i]:
                if contact in used: add = False
                new_used.add(contact)

            used |= new_used
            if add: ans += 1

        return ans
