class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        first, count = 0, 0
        g.sort()
        s.sort()
        for second in range(len(s)):
            while first < len(g):
                if s[second] >= g[first]:
                    count += 1
                    first += 1
                break
        return count