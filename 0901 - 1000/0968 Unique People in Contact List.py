class Solution:
    def solve(self, contacts):
        ans = 0
        s = set()

        for contact in contacts:
            ans += not any(email in s for email in contact)
            s |= set(contact)

        return ans
