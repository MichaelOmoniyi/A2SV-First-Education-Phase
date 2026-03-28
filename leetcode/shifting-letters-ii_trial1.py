class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * n

        for l, r, k in shifts:
            val = 1 if k == 1 else -1
            diff[l] += val
            if r + 1 < n:
                diff[r + 1] -= val

        for i in range(1, n):
            diff[i] += diff[i - 1]

        res = []
        for i in range(n):
            shift = diff[i] % 26
            newChar = (ord(s[i]) - ord('a') + shift) % 26
            res.append(chr(newChar + ord('a')))
        return "".join(res)