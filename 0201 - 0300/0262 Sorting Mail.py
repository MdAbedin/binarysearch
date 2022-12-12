class Solution:
    def solve(self, mailboxes):
        ans = []
        cols = defaultdict(list)
        max_mailbox_len = 0

        for mailbox in mailboxes:
            max_mailbox_len = max(max_mailbox_len, len(mailbox))
            for c in range(len(mailbox)):
                cols[c].append(mailbox[c])

        for c in range(max_mailbox_len):
            for mail in cols[c]:
                if mail != "junk": ans.append(mail)

        return ans
