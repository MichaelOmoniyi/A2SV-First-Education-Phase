class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = 0, len(cardPoints) - k
        total = sum(cardPoints[right:])
        score = total

        while right < len(cardPoints):
            total += (cardPoints[left] - cardPoints[right])
            score = max(score, total)

            right += 1
            left += 1
        return score