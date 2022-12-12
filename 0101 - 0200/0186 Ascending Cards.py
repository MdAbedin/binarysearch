class Solution:
    def solve(self, cards):
        if not cards: return []
        cards.sort()
        ans = [-1]*len(cards)
        deck = deque(range(len(cards)))
        expecting = 0
        while deck:
            ans[deck.popleft()] = cards[expecting]
            expecting += 1
            if deck:
                deck.append(deck.popleft())
        return ans
