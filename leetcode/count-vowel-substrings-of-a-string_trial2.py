class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        lastSeen = {}
        left = 0
        res = 0

        for right, c in enumerate(word):

            if c not in vowels:
                lastSeen.clear()
                left = right + 1
                continue

            lastSeen[c] = right

            if len(lastSeen) == 5:
                res += min(lastSeen.values()) - left + 1

        return res