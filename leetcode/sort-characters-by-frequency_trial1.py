from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        sCounter = Counter(s)
        sCounterSorted = sorted(sCounter.items(), key= lambda x: x[1], reverse=True)
        ans = ""

        for char in sCounterSorted:
            for i in range(char[1]):
                ans += char[0]
        return(ans)
        