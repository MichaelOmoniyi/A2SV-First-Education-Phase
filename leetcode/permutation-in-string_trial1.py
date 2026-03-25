class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        window = [0] * 26

        for char in s1:
            s1Count[ord(char) - ord('a')] += 1

        k = len(s1)

        for i in range(len(s2)):
            window[ord(s2[i]) - ord('a')] += 1

            if i >= k:
                window[ord(s2[i - k]) - ord('a')] -= 1

            if window == s1Count:
                return True
        return False