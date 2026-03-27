class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left, longest = 0, 0

        for right in range(len(s)):
            while window and s[right] in window:
                window.discard(s[left])
                left += 1
            window.add(s[right])
            longest = max(longest, len(window))
        return longest