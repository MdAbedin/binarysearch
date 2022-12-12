import re
class Solution:
    def solve(self, text, patterns):
        if not text or not patterns: return text

        starts = {m.start() for pattern in patterns for m in finditer(f"(?={pattern})", text)}
        ends = {m.start() + len(pattern) for pattern in patterns for m in finditer(f"(?={pattern})", text)}

        ans = []
        open_tag,close_tag = "<b>","</b>"
        level = 0

        for i,char in enumerate(text):
            if i in starts and i in ends:
                pass
            elif i in starts:
                if level == 0:
                    if ans and ans[-1] == close_tag:
                        ans.pop()
                    else:
                        ans.append(open_tag)
                level += 1
            elif i in ends:
                if level == 1:
                    ans.append(close_tag)
                level -= 1

            ans.append(char)

        if len(text) in ends: ans.append(close_tag)

        return "".join(ans)
