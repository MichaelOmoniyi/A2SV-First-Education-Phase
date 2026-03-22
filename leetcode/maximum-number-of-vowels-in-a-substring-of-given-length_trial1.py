class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        count = 0

        for i in range(k):
            if s[i] in vowel:
                count += 1
        maxCount = count

        for i in range(k, len(s)):
            if s[i] in vowel:
                count += 1

            if s[i - k] in vowel:
                count -= 1

            maxCount = max(count, maxCount)

        return maxCount